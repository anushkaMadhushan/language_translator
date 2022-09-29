from translate import Translator
translator = Translator(from_lang="english", to_lang="japanese")
translation=translator.translate("Hello")
print(translation)
