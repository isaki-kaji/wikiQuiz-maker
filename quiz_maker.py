import wikipedia
import re
import MeCab
import neologdn
import datetime
wikipedia.set_lang("ja")


def count_overlap(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i:] in str2:
            count += 1
    return count


def set_document(title_list, category, min_text_len, min_textlist_len):
    tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
    for title in title_list:
        try:
            add_text_list = []
            final_list = []
            page = wikipedia.page(title)
            text_list = page.content.strip().split("\n")
            for text in text_list:
                text = re.sub(r'[\(\（][^()\（\）]*[\)\）]', '', text)
                nihongo_text = re.sub(r"[\a-zA-Z0-9_]", "", text)
                if (len(nihongo_text) > min_text_len):
                    add_text_list.append(text)
                if (len(add_text_list) > min_textlist_len):
                    taggered_list = []
                    for re_text in add_text_list:
                        parsed_text = tagger.parse(re_text)
                        parsed_words = parsed_text.split("\n")
                        for i in parsed_words:
                            index = i.find("\t")
                            if index != -1:
                                result = i[:index]
                                if ((result == title) or ((count_overlap(result, title)-len(result) == 0) and (len(result) > 1 and (bool(re.match(r'^[\u4E00-\u9FD0]+$', result)) == True)))):
                                    result = "〇〇"
                                taggered_list.append(result)
                        final_list.append(taggered_list)
            doc_ref = db.collection(category).document(title)
            doc_ref.set({
                "title": title,
                "text": final_list,
                "url": page.url,
                "更新日": datetime.date.today(),
            })
        except:
            pass
