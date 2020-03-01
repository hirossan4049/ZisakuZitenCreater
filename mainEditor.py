import json
from pprint import pprint

from kivy.logger import Logger
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleboxlayout import RecycleBoxLayout


class ListItem(BoxLayout):
    index = StringProperty()
    ztitle = StringProperty()
    zcontent = StringProperty()

    # def refresh_view_attrs(self, rv, index, data):
    #     ''' Catch and handle the view changes '''
    #     self.index = index
    #     print(self.index)
    #     self.label1_text = str(index)
    #     self.label2_text = data['label2']['text']
    #     self.ids['id_label3'].text = data['label3']['text']  # As an alternate method of assignment
    #     print("ref")
    #     return super(ListItem, self).refresh_view_attrs(
    #         rv, index, data)


class MainEditor(BoxLayout):
    def __init__(self, **kwargs):
        super(MainEditor, self).__init__(**kwargs)
        self.maxIndex = 0

        self.set()

    def read(self, path):
        self.path = path
        self.open()

    def open(self):
        try:
            with open(self.path, "r") as jj:
                self.json = json.load(jj)
        except FileNotFoundError:
            Logger.info("FileNotFound! json.load pass!")
            with open("template.json", "r") as jj:
                self.json = json.load(jj)
        # self.jsonfile = json.lo_ad(open(path,"r"))
        Logger.info("path" + self.path)
        pprint(self.json)
        # self.save()

    def save(self):
        with open(self.path, "w") as jj:
            json.dump(self.json, jj, ensure_ascii=False)

    def set(self):
        for i in range(1, 10):
            self.maxIndex += 1
            self.ids.rv.data.append({"index": str(self.maxIndex), "ztitle": "title", "zcontent": "content"})
        # print(self.ids.rv.data)

    def add(self):
        print("add")
        viewadapter = self.ids.rv.view_adapter
        print(viewadapter.views)
        pos = self.ids.rv.to_local(self.ids.rv.center_x, self.ids.rv.height)
        print(self.ids.rv.viewclass)
        print(self.ids.rv.layout_manager.get_view_index_at(pos))

        for i in range(1,self.maxIndex+1):
            try:
                print(viewadapter.get_visible_view(i).ids.ztitleInput.text)
            except:
                print("error")

        # RecycleBoxLayout
