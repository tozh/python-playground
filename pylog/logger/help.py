# coding=utf-8

# from common.rpc.notice import send_text_notice
import re
import os
from local_log import LocalLog
import time
import threading

class SendNotice():
    def __init__(self, path):
        self.path = path
        self.task = 'notice'
        self.err_count = 0

    # def send_notice(self, uid):
    #     title = u'故事功能维护'
    #     content = u'抖音的个人故事功能维护，将暂时下线。如有需要，请尽快将已发布的故事保存到本地。如有不便，非常抱歉。'
    #     send_text_notice(uid, title, content)

    def record_process(self, file, i):
        process_file = os.path.join(self.path, 'process/', file + '.process')
        with open(process_file, 'a+') as f:
            f.write(str(i) + '\n')
            f.close()

    def read_file(self, file, logger, start_line=-1):
        file_path = os.path.join(self.path, file)
        with open(file_path, 'r') as f:
            for i, line in enumerate(f):
                if i > start_line:
                    if line.strip():
                        try:
                            uid = long(line.strip())
                        except Exception as err:
                            logger.error(file, i, line.strip(), 1, err, line)
                            print line
                            continue
                        try:
                            # self.send_notice(uid)
                            logger.info(file, i, uid, 0)

                        except Exception as err:
                            logger.error(file, i, uid, 1, err, uid)
                    if i % 500 == 0:
                        self.record_process(file, i)
                        # time.sleep(0.01)
            f.close()

    def excute(self):
        rough_file_list = sorted(os.listdir(self.path))
        file_list = []
        idx = 0
        for file in rough_file_list:
            print file
            file_path = os.path.join(self.path, file)
            if 'process' not in file and not os.path.isdir(file_path):
                file_list.append(file)

        while idx < len(file_list):
            print 'idx:', idx
            threads = []
            for file in file_list[idx:idx+5]:
                print 'file:', file
                file_path = os.path.join(self.path, file)
                if 'process' not in file and not os.path.isdir(file_path):
                    start_line = self.read_start_line(file)
                    logger = LocalLog(self.task, self.path, 'log/', file)
                    print 'start_line:', start_line
                    t = threading.Thread(target=self.read_file, args=(file, logger, start_line))
                    threads.append(t)

            for t in threads:
                t.start()
            for t in threads:
                t.join()
            idx += 5

    def read_start_line(self, file):
        log_file_list = os.listdir(os.path.join(self.path, 'log/'))
        if 'notice_' + file + '_info.log' in log_file_list:
            info_log = os.path.join(self.path, 'log/', 'notice_' + file + '_info.log')
        else:
            info_log = None
        if 'notice_' + file + '_error.log' in log_file_list:
            error_log = os.path.join(self.path, 'log/', 'notice_' + file + '_error.log')
        else:
            error_log = None
        max_line_idx = -1
        if info_log:
            with open(info_log, 'r') as f:
                for line in f:
                    line_idx, uid = self.recognize_log_line(line)
                    max_line_idx = line_idx if line_idx > max_line_idx else max_line_idx
        if error_log:
            with open(error_log, 'r') as f:
                for line in f:
                    line_idx, uid = self.recognize_log_line(line)
                    max_line_idx = line_idx if line_idx > max_line_idx else max_line_idx
        return max_line_idx

    # def read_error_log(self):
    #     log_file_list = sorted(os.listdir(os.path.join(self.path, 'log/')))
    #     for file in log_file_list:
    #         if 'error' in file:
    #             file_path = os.path.join(self.path, 'log/', file)
    #             logger = LocalLog(self.task, self.path, 'log2/', file)
    #             with open(file_path, 'r') as f:
    #                 for i, line in enumerate(f):
    #                     if line.strip():
    #                         try:
    #                             _, uid = self.recognize_log_line(line)
    #                         except Exception as err:
    #                             print line
    #                             logger.error(file, i, line.strip(), 1, err, line)
    #                             continue
    #                         try:
    #                             # self.send_notice(uid)
    #                             logger.info(file, i, uid, 0)
    #                         except Exception as err:
    #                             logger.error(file, i, uid, 1, err, line)
    #                 f.close()

    def recognize_log_line(self, line):
        line_idx = int(line.split('Line: ')[1].split(', Time')[0])
        uid = long(line.split('Uid: ')[1].split(', Result')[0])
        return line_idx, uid


if __name__ == '__main__':
    # from frame import default_settings
    # from frame import rpc
    #
    # default_settings.ENABLE_RPC = True
    # # default_settings.DEBUG = True
    # rpc.init(default_settings)
    # path = '/data00/users/zhaotong.zt/fs_data/story_user_id/'
    path = '/data00/users/zhaotong.zt/zt/'
    t1 = time.time()
    sn = SendNotice(path)
    sn.excute()
    t2 = time.time()
    print 'time:', t2-t1
    # sn.read_error_log()

