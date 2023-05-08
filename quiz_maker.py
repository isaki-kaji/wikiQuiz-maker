import wikipedia
import re
import MeCab
import neologdn
wikipedia.set_lang("ja")

def set_document(title_list,category,min_text_len,min_textlist_len):
    tagger=MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
    for title in title_list:
        add_text_list=[]
        text_list=wikipedia.page(title).content.strip().split("\n")
        for text in text_list:
            text=re.sub(r'[\(\（][^()\（\）]*[\)\）]', '', text)
            nihongo_text=re.sub(r"[\a-zA-Z0-9_]","",text)
            if(len(nihongo_text)>min_text_len):
                add_text_list.append(text)
            if(len(add_text_list)>min_textlist_len):
                for re_text in add_text_list:
                    parsed_text=tagger.parse(re_text)
                    parsed_words=parsed_text.split("\n")
                    for word in parsed_words:
                