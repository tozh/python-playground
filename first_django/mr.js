// var followers_map = function() { emit(this.num, {"times":[this.time]});} ;

// var followers_reduce = function(key, values) {
//     var ref = {
//         times:[]
//     };
//     var id = {};
//     for(var i in values) {
//         var v = values[i];
//         for (var j in v.times)
//         if (!id[v.times[j]]) {
//             id[v.times[j]] = true;
//             ref.times.push(v.times[j]);
//         }
//     }
//     return ref;
// };


// var followers_options = {
//     out: "mytry2",

// };

// db.mytry.mapReduce(followers_map, followers_reduce, followers_options )

var followers_map = function() { emit(this.self_id, {"data":[this.followed_by]});} ;

var followers_reduce = function(key, values) {
    var ref = {
        data:[]
    };
    var id = {};
    for(var i in values) {
        var v = values[i];
        for (var j in v.data)
        if (!id[v.data[j]]) {
            id[v.data[j]] = true;
            ref.data.push(v.data[j]);
        }
    }
    return ref;
};


var followers_options = {
    out: "followers",
    jsMode: true
};

db.followedBy.mapReduce(followers_map, followers_reduce, followers_options )

// var randomFrom = function (start, end) {
//         var length = end - start + 1;
//         var num = parseInt(Math.random() * (length) + start);
//         return num;
//     };

// for (var i=0; i<100; i++) {
//     var times = randomFrom(1001, 3000);
//     for(var j=0; j < times; j++) {
//         db.mytry.insert({num: i, time: times});
//     }
// }



// db.followedBy.aggregate(
//             [
//                   {
//                         $group:{

//                               _id: {self_id: "$self_id", followed_by: "$followed_by"},
//                               self_id: {$push: "$self_id"},
//                               followed_by: {$push: "$followed_by"}
//                         }
//                   }
//             ]
//         ). forEach(function(x){
//             db.followedBy_2.insert(
//                   {
//                     self_id : x.self_id[0],
//                     followed_by: x.followed_by[0]                    
//                   }
//             );
//         });

// var myresult = db.haha.aggregate(
//     [
//           {
//                 $group:{
                    
//                       _id: {self_if: "$self_id", followed_by: "$followed_by"},
//                 }
//           }
//     ]
// );
// printjson(myresult);

var followers_fe = function(entry) {
    var key = entry['_id'];
    var arr = entry['value']['data'];
    db.users.update({'_id':key}, {$set:{"followers":arr}})
};

var cursor1 = db.followers.find()
cursor1.forEach(followers_fe);



var followedByChange = function(entry) {
    id = entry["self_id"]
    fo = entry["followed_by"]
    db.followedBy2.insert({"self_id":id, "followed_by":fo});
};
var cursor = db.followedBy.find().noCursorTimeout();
cursor.forEach(followedByChange);


var followees_map = function() { emit(this.followed_by,{"data":[this.self_id]});};

var followees_reduce = function(key, values) {
    var ref = {
        data:[]
    };
    var id = {};
    for(var i in values) {
        var v = values[i];
        for (var j in v.data)
        if (!id[v.data[j]]) {
            id[v.data[j]] = true;
            ref.data.push(v.data[j]);
        }
    }
    return ref;
};

var followees_options = {
    out: "followees",
    jsMode: true
};

 db.followedBy.mapReduce(followees_map, followees_reduce, followees_options )

var followees_fe = function(entry) {
    var key = entry['_id'];
    var arr = entry['value']['data'];
    db.users.update({'_id':key}, {$set:{"followees":arr}})
};

var cursor2 = db.followees.find()
cursor2.forEach(followees_fe);







