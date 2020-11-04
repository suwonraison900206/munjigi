from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .serializers import HeritageSerializer, HeritageDetailSerializer, HeritageRatingSerializer, UserTagSerializer
from .models import Heritage, Heritage_rating, User_tag, Tag
from backend.pagination import CustomPagination
from django.db.models import Count, Q, Avg
from accounts.models import User
from .recommend import recommend_system


class HeritageListAPI(GenericAPIView):
    serializer_class = HeritageSerializer
    queryset = Heritage.objects.all()
    pagination_class = CustomPagination

    
    def get(self, request):
        sort = request.GET.get('sort','')
        query = request.GET.get('query', '')
        if sort == 'likes':
            queryset = Heritage.objects.annotate(like_count=Count('like_users')).order_by('-like_count')
            if query:
                queryset = queryset.filter(Q (k_name__icontains=query) | Q (content__icontains=query)).order_by('-hit')
        else:
            queryset = self.filter_queryset(self.get_queryset())
            if query:
                queryset = queryset.filter(Q (k_name__icontains=query) | Q (content__icontains=query)).order_by('-hit')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data # pagination data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
        payload = {
            'return_code': '0000',
            'return_message': 'Success',
            'data': data
        }
        return Response(data)


class HeritageListAPI2(GenericAPIView):
    serializer_class = HeritageSerializer
    queryset = Heritage.objects.all()
    pagination_class = CustomPagination
    def get(self, request):
        sort = request.GET.get('sort','')
        query = request.GET.get('query', '')
        if sort == 'likes':
            queryset = Heritage.objects.annotate(like_count=Count('like_users')).order_by('-like_count')
            if query:
                queryset = queryset.filter(Q (k_name__icontains=query)).order_by('-hit')
        else:
            queryset = self.filter_queryset(self.get_queryset())
            if query:
                queryset = queryset.filter(Q (k_name__icontains=query)).order_by('-hit')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data # pagination data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
        payload = {
            'return_code': '0000',
            'return_message': 'Success',
            'data': data
        }
        return Response(data)


class HeritageDetailAPI(generics.GenericAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageDetailSerializer

    def get(self ,request, pk):
        heritage = get_object_or_404(Heritage, pk=pk)
        if request.session.get("h_hit", False) == False:
            request.session["h_hit"] = []
        hit_l = request.session["h_hit"]
        if pk not in hit_l:
            hit_l.append(pk)
            request.session["h_hit"] = hit_l
            heritage.hit += 1
        
        h_data = HeritageDetailSerializer(heritage).data
        serializer = HeritageDetailSerializer(heritage, data = h_data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.data)



class HeritageLikeAPI(generics.GenericAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageDetailSerializer
    permissions_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        heritage = get_object_or_404(Heritage, pk=pk)
        user = User.objects.get(id=request.data['userDataId'])
        if user in heritage.like_users.all():
            heritage.like_users.remove(user)
            user_remove_weight(request.data['userDataId'], pk)
        else:
            heritage.like_users.add(user)
            user_add_weight(request.data['userDataId'], pk)
        serializer = HeritageDetailSerializer(heritage)
        return Response(serializer.data)


#서베이용
class Survey_weightAPI(generics.GenericAPIView):
    # queryset = Heritage.objects.all()
    # serializer_class = HeritageDetailSerializer
    

    permissions_classes = [permissions.IsAuthenticated]
    def post(self, request):
        check_user = User.objects.get(email=request.user)
        print(check_user)
        if check_user.survey == True:
        
            return Response()

        check_user.survey = True
        check_user.save()
        Survey_weight_df(request.user, request.body)
        return Response()


class HeritageBookmarkAPI(generics.GenericAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageDetailSerializer
    permissions_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        heritage = get_object_or_404(Heritage, pk=pk)
        user = User.objects.get(id=request.data['userDataId'])
        if user in heritage.dib_users.all():
            heritage.dib_users.remove(user)
            user_remove_weight(request.data['userDataId'], pk)
        else:
            heritage.dib_users.add(user)
            user_add_weight(request.data['userDataId'], pk)
        serializer = HeritageDetailSerializer(heritage)
        return Response(serializer.data)


class HeritageVisitAPI(generics.GenericAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageDetailSerializer
    permissions_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        heritage = get_object_or_404(Heritage, pk=pk)
        user = User.objects.get(id=request.data['userDataId'])
        if user in heritage.visit_users.all():
            heritage.visit_users.remove(user)
        else:
            heritage.visit_users.add(user)
        serializer = HeritageDetailSerializer(heritage)
        return Response(serializer.data)


class HeritageRatingAPI(generics.GenericAPIView):
    queryset = Heritage_rating.objects.all()
    serializer_class = HeritageRatingSerializer
    def get(self, request, pk):
        queryset = Heritage_rating.objects.filter(Q(heritage_id=pk))
        serializer = HeritageRatingSerializer(queryset, many=True)
        return Response(serializer.data)
    

    def post(self, request, pk):
        queryset = Heritage_rating.objects.filter(heritage_id=pk)
        serializer = HeritageRatingSerializer(queryset, many=True)
        
        for serializerData in serializer.data:
            if serializerData['user'] == int(request.data['user']):
                queryset = Heritage_rating.objects.filter(Q(heritage_id=pk) & Q(user_id=request.data['user'])).first()
                heritage_rate = Heritage_rating.objects.get(heritage_id=pk, user_id = request.data['user']).rating
                serializer = HeritageRatingSerializer(queryset, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    user_rating_weight(request.data['user'], pk, request.data['rating'], heritage_rate)
                    rating_average(pk)
                    queryset = Heritage_rating.objects.filter(heritage_id=pk)
                    serializer = HeritageRatingSerializer(queryset, many=True)
                    return Response(serializer.data)
        else:
            serializer = HeritageRatingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                user_rating_weight(request.data['user'], pk, request.data['rating'], 0)
                rating_average(pk)
                queryset = Heritage_rating.objects.filter(heritage_id=pk)
                serializer = HeritageRatingSerializer(queryset, many=True)
                return Response(serializer.data)


class HeritageRecommendationAPI(generics.GenericAPIView):
    serializer_class = HeritageSerializer
    queryset = Heritage.objects.all()
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        heritage_recommend = recommend_system(user.pk)
        queryset = Heritage.objects.filter(pk__in=heritage_recommend)
        serializer = HeritageSerializer(queryset, many=True)
        return Response(serializer.data)


# 문화재 평균 평점
def rating_average(heritage_id):
    avg_rating = Heritage_rating.objects.filter(heritage_id=heritage_id).aggregate(Avg('rating'))
    heritage = Heritage.objects.get(id=heritage_id)
    heritage.rating = avg_rating['rating__avg']
    heritage.save()
    return


# 문화재 좋아요 및 북마크시 가중치 설정
def user_add_weight(user_id, heritage_id):
    tag_queryset = Heritage.objects.filter(pk=heritage_id).values('heritage_tags')
    user_queryset = User_tag.objects.filter(user_id=user_id).values('tag_id')
    tagging = []
    u_tagging = []
    for tag in tag_queryset:
        tagging.append(tag['heritage_tags'])
    for u_tag in user_queryset:
        u_tagging.append(u_tag['tag_id'])
    
    for tag in tagging:
        if tag in u_tagging:
            user_tag = User_tag.objects.get(user_id = user_id, tag_id = tag)
            user_tag.weight += 1
            user_tag.save()
        else:
            user_tag = User_tag.objects.create(user_id = user_id, tag_id = tag)
            user_tag.weight += 1
            user_tag.save()
    return

#서베이용
def Survey_weight_df(user_id, tag_l):
    userid = User.objects.get(email = user_id).id
    tagging = tag_l.decode("utf-8")
    tn = 0
    tag_test = []
    tag_word = ""
    for tt in tagging:
        if tt == '"':
            tn += 1
            continue
        tn = tn % 2
        if tn == 1:
            tag_word += tt
        elif tn == 0:
            if tag_word == "":
                continue
            tag_test.append(tag_word)
            tag_word = ""
    tag_test2 = []
    for tg in tag_test:
        tag_test2.append(Tag.objects.get(name = tg))
    tagging = []
    for tag in tag_test2:
        tagging.append(tag.id)
    user_queryset = User_tag.objects.filter(user_id=user_id).values('tag_id')
    u_tagging = []
    for u_tag in user_queryset:
        u_tagging.append(u_tag['tag_id'])
    for tag in tagging:
        if tag in u_tagging:
            user_tag = User_tag.objects.get(user_id = userid, tag_id = tag)
            user_tag.weight += 1
            user_tag.save()
        else:
            user_tag = User_tag.objects.create(user_id = userid, tag_id = tag)
            user_tag.weight += 1
            user_tag.save()
    return


# 문화재 좋아요 및 북마크 취소시 가중치 감소
def user_remove_weight(user_id, heritage_id):
    tag_queryset = Heritage.objects.filter(pk=heritage_id).values('heritage_tags')
    user_queryset = User_tag.objects.filter(user_id=user_id).values('tag_id')
    tagging = []
    u_tagging = [] 
    for tag in tag_queryset:
        tagging.append(tag['heritage_tags'])
    for u_tag in user_queryset:
        u_tagging.append(u_tag['tag_id'])
    for tag in tagging:
        if tag in u_tagging:
            user_tag = User_tag.objects.get(user_id = user_id, tag_id = tag)
            user_tag.weight -= 1
            user_tag.save()
        else:
            user_tag = User_tag.objects.create(user_id = user_id, tag_id = tag)
            user_tag.weight -= 1
            user_tag.save()
    return


# 문화재 평점 추가 및 수정 시 가중치 수정
def user_rating_weight(user_id, heritage_id, current_rating, bef_rating):
    tag_queryset = Heritage.objects.filter(pk=heritage_id).values('heritage_tags')
    user_queryset = User_tag.objects.filter(user_id=user_id).values('tag_id')
    tagging = []
    u_tagging = []
    for tag in tag_queryset:
        tagging.append(tag['heritage_tags'])
    for u_tag in user_queryset:
        u_tagging.append(u_tag['tag_id'])
    for tag in tagging:
        if tag in u_tagging:
            user_tag = User_tag.objects.get(user_id = user_id, tag_id = tag)
            user_tag.weight -= bef_rating
            user_tag.weight += current_rating
            user_tag.save()
        else:
            user_tag = User_tag.objects.create(user_id = user_id, tag_id = tag)
            user_tag.weight -= bef_rating
            user_tag.weight += current_rating
            user_tag.save()
    return