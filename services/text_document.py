from docxtpl import DocxTemplate, RichText
import base64
import uuid
import re
from datetime import date

class DocumentCreator:
    def __init__(self):
        pass

    def documentify(self, topics, titles, summarys, urls, domains):
        doc = DocxTemplate("services/Pressespiegel_Template.docx")
        url_con = {}
        date_ = {}
        date_["date"] = date.today().strftime("%d.%m.%Y")
        

        for x in range(10):
            for y in range(10):
                if "url{}_{}".format(x, y) in urls and urls["url{}_{}".format(x, y)] != "":
                    url_con["url{}_{}".format(x, y)] = RichText("")
                    url_con["url{}_{}".format(x, y)].add(domains["domain{}_{}".format(x, y)], url_id=doc.build_url_id(urls["url{}_{}".format(x, y)]))

        context = url_con | topics | titles | summarys | date_
        doc.render(context)
        doc.save("services/Pressespiegel_{}.docx".format(date.today().strftime("%d.%m.%Y")))

    def download_document(self, file, file_name, button_text):
        b64 = base64.b64encode(file).decode()

        button_uuid = str(uuid.uuid4()).replace('-', '')
        button_id = re.sub('\d+', '', button_uuid)

        custom_css = f""" 
            <style>
                #{button_id} {{
                    background-color: rgb(255, 255, 255);
                    color: rgb(38, 39, 48);
                    padding: 0.25em 0.38em;
                    position: relative;
                    text-decoration: none;
                    border-radius: 4px;
                    border-width: 1px;
                    border-style: solid;
                    border-color: rgb(230, 234, 241);
                    border-image: initial;
                }} 
                #{button_id}:hover {{
                    border-color: rgb(246, 51, 102);
                    color: rgb(246, 51, 102);
                }}
                #{button_id}:active {{
                    box-shadow: none;
                    background-color: rgb(246, 51, 102);
                    color: white;
                    }}
            </style> """

        dl_link = custom_css + f'<a download="{file_name}" id="{button_id}" href="data:file/txt;base64,{b64}">{button_text}</a><br></br>'

        return dl_link