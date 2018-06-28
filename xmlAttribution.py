
class XmlAttr(object):
    def __init__(self):
        self.filename = ''
        self.fileshape = []
        self.bboxes = []

    @property
    def get_filename(self):
        return self.filename

    @property
    def get_fileshape(self):
        return self.fileshape

    @property
    def get_bboxes(self):
        return self.bboxes

    def set_filename(self, filename):
        if not isinstance(filename, str):
            raise TypeError('filename must be type of string!')
        self.filename = filename

    def set_fileshape(self, fileshap):
        if not isinstance(fileshap, list):
            raise TypeError('fileshape must be type of list!')
        self.fileshape = fileshap

    def set_bbox(self, bboxes):
        if not isinstance(bboxes, list):
            raise TypeError('bbox must be type of list!')
        self.__sort_bboxes(bboxes)
        self.bboxes = bboxes

    def __sort_bboxes(self, bboxes):
        need_stop = False
        for i in range(len(bboxes)):
            need_stop = True
            for j in range(i + 1, len(bboxes)):
                if bboxes[i][0] > bboxes[j][0]:
                    tmp = bboxes[j]
                    bboxes[j] = bboxes[i]
                    bboxes[i] = tmp
                    need_stop = False
            if need_stop:
                break

    def __str__(self):
        if 3 == len(self.fileshape):
            return 'The file name is : %s, file shape is : %s*%s*%s, ' \
               'length of bbox is: %s!' %(self.filename, self.fileshape[0],
                                         self.fileshape[1], self.fileshape[2], len(self.bboxes))
        elif 2 == len(self.fileshape):
            return 'The file name is : %s, file shape is : %s*%s*%s, ' \
               'length of bbox is: %s!' %(self.filename, self.fileshape[0],
                                         self.fileshape[1], len(self.bboxes))
        else:
            return 'Sorry, some error happened!'