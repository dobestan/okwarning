from django.views.generic import TemplateView


class NewWarningTemplateView(TemplateView):
    template_name = 'new.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(*args, **kwargs)

        # 불법·유해정보사이트에 대한 차단 안내
        # http://warning.or.kr/

        context['categories'] = [
            {
                'name': '안보위해행위',  # 사이트 분야
                'agencies': [
                    {
                        'name': '사이버경찰청',  # 담당기관
                        'contact': '1566-0112',  # 전화번호
                    },
                ],
            },
            {
                'name': '도박',
                'agencies': [
                    {
                        'name': '사이버경찰청',
                        'contact': '1566-0112',
                    },
                    {
                        'name': '사행산업통합감독위원회',
                        'contact': '(02)3704-0538',
                    },
                ],
            },
            {
                'name': '음란',
                'agencies': [
                    {
                        'name': '방송통신심의위원회',
                        'contact': '(02)3219-5152, 5153',
                    },
                ],
            },
            {
                'name': '불법 의약품 판매',
                'agencies': [
                    {
                        'name': '식품의약품안전처 의약품관리총괄과',
                        'contact': '(043)719-2657',
                    },
                ],
            },
            {
                'name': '불법 식품 판매 및 허위과대광고',
                'agencies': [
                    {
                        'name': '식품의약품안전처 식품관리총괄과',
                        'contact': '(043)719-2063',
                    },
                ],
            },
            {
                'name': '불법 건강기능식품 판매 및 허위과대광고',
                'agencies': [
                    {
                        'name': '식품의약품안전처 건강기능식품정책과',
                        'contact': '(043)719-2468',
                    },
                ],
            },
            {
                'name': '불법 화장품 판매 및 허위과대광고',
                'agencies': [
                    {
                        'name': '식품의약품안전처 화장품정책과',
                        'contact': '(043)719-3407',
                    },
                ],
            },
            {
                'name': '불법 의료기기 판매',
                'agencies': [
                    {
                        'name': '식품의약품안전처 의료기기관리과',
                        'contact': '(043)719-3762',
                    },
                ],
            },
            {
                'name': '불법 마약류 매매',
                'agencies': [
                    {
                        'name': '식품의약품안전처 마약정책과',
                        'contact': '(043)719-2806',
                    },
                ],
            },
            {
                'name': '불법 체육진흥투표권 판매',
                'agencies': [
                    {
                        'name': '사행산업통합감독위원회',
                        'contact': '(02)3704-0538',
                    },
                    {
                        'name': '국민체육진흥공단 클린스포츠 통합콜센터',
                        'contact': '1899-1119',
                    },
                ],
            },
            {
                'name': '불법 승자투표권 구매대행',
                'agencies': [
                    {
                        'name': '국민체육진흥공단 경륜사업본부',
                        'contact': '(02)2067-5813',
                    },
                    {
                        'name': '국민체육진흥공단 경정사업본부',
                        'contact': '(031)790-8531',
                    },
                ],
            },
            {
                'name': '불법 마권 구매대행',
                'agencies': [
                    {
                        'name': '한국마사회',
                        'contact': '080-8282-112',
                    },
                ],
            },
            {
                'name': '상표권(위조상품 유통)',
                'agencies': [
                    {
                        'name': '한국지식재산보호협회',
                        'contact': '(02)2183-5834',
                    },
                ],
            },
            {
                'name': '저작권(불법복제물 유통)',
                'agencies': [
                    {
                        'name': '한국저작권위원회 침해정보심의팀',
                        'contact': '(055)792-0182',
                    },
                ],
            },
        ]

        # 운영자 이의신청 안내
        context['objections'] = [
            {
                'content': '도박',  # 정보내용
                'contact': '(02)3219-5133',  # 전화번호
            },
            {
                'content': '식의약품',
                'contact': '(02)3219-5143',
            },
            {
                'content': '국가보안법 등',
                'contact': '(02)3219-5142',
            },
            {
                'content': '음란·선정',
                'contact': '(02)3219-5152, 5153',
            },
            {
                'content': '명예훼손',
                'contact': '(02)3470-6734',
            },
            {
                'content': '잔혹·혐오, 차별비하',
                'contact': '(02)3219-5162',
            },
        ]

        return context
