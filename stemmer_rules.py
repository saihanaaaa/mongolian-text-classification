# code from https://github.com/erkhemee/chatbot-ub-hackathon

stemmer_rules_tuple = ("ы$|ий$|ыг$|ийг$|ны$|ний$|лаа$|лээ$|лоо$|лөө$|даа$|дээ$|доо$|дөө$|уулж$|үүлж$|гдах$|гдэх$|гдох$|гдөх$|лалт$|лэлт$|лолт$|лөлт$|дахад$|дэхэд$|доход$|дөхөд$|уудыг$|үүдийг$|нүүдийг$|нуудыг$|чихлаа$|чихлээ$|чихлоо$|чихлөө$|ид$|ын$|ийн$|уудын$|үүдийн$|тай$|той$|төй$|тэй$|лал$|лэл$|лол$|лөл$|аар$|ээр$|оор$|өөр$|лах$|лэх$|лох$|лөх$|ахад$|эхэд$|оход$|өхөд$|лалд$|лэлд$|лөлд$|лолд$|ууд$|үүд$|даг$|дэг$|дог$|дөг$|ддаг$|ддэг$|ддог$|ддөг$|даж$|дэж$|дож$|дөж$|сэн$|сан$|сөн$|сон$|гах$|гэх$|гох$|гөх$|рах$|рэх$|рох$|рөх$|иас$|иэс$|иос$|иөс$|нд$|нт$|ад$|эд$|од$|өд$|ааж$|ээж$|оож$|өөж$|лаар$|лээр$|лоор$|лөөр$|аг$|эг$|ог$|өг$|уг$|өөг$|ээг$|оог$|үүг$|ууг$|бар$|бэр$|бор$|бөр$|бур$|бүр$|раа$|рээ$|рөө$|рүү$|роо$|руу$|аас$|ээс$|оос$|өөс$|аарх$|ээрх$|оорх$|уурх$|үүрх$|өөрх$|аад$|ээд$|ууд$|үүд$|оод$|өөд$|нууд$|нүүд$|дсан$|дсэн$|дсөн$|дсон$|дах$|дэх$|дох$|дөх$|хлаа$|хлээ$|хлоо$|хлөө$|лахдаа$|лэхдээ$|лохдоо$|лөхдөө$|лдаг$|лдэг$|лж$|аагүй$|ээгүй$|оогүй$|өөгүй$|даггүй$|дэггүй$|доггүй$|дөггүй$|нуудийнхаа$|нүүдийнхээ$|гүй$")