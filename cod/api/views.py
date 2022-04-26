from rest_framework import viewsets, mixins, permissions
from rest_framework.generics import get_object_or_404
from .models import *
from .serializers import *
from datetime import datetime
from django.db.models import Q



class PermissionMixin:
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete']:
            permission_list = [permissions.IsAdminUser, ]
        else:
            permission_list = [permissions.IsAuthenticated, ]
        # elif self.action in ['create', 'update', 'partial_update', 'delete']:
        #     permission_list = [permissions.IsAdminUser, ]
        
        # else:
        #     permission_list = []
        return [perm() for perm in permission_list]






class QuizViewSet(PermissionMixin, viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionViewSet(PermissionMixin, viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz = get_object_or_404(Quiz, id=self.kwargs['id'])
        return quiz.questions.all()

    def perform_create(self, serializer):
        quiz = get_object_or_404(Quiz, pk=self.kwargs['id'])
        serializer.save(quiz=quiz)


class ChoiceViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        question = get_object_or_404(Question, id=self.kwargs['question_pk'])
        return question.choices.all()

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs['question_pk'], quiz__id=self.kwargs['id'])
        serializer.save(question=question)


class AnswerViewSet(PermissionMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_serializer_class(self):
        question = get_object_or_404(Question, pk=self.kwargs['question_pk'], quiz__id=self.kwargs['id'])

        if question.type == 'text_answer':
            return TextSerializer
        elif question.type == 'one_answer':
            return OneAnswerSerializer
        else:
            return MultipleAnswersSerializer

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs['question_pk'], quiz__id=self.kwargs['id'])
        serializer.save(user=self.request.user, question=question)


class ActiveQuizListViewSet(PermissionMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Quiz.objects.filter(end__gte=datetime.today())
    serializer_class = QuizSerializer


class UserListViewSet(PermissionMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserQuizSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Quiz.objects.exclude(~Q(questions__answers__user__id=user_id))
        return queryset