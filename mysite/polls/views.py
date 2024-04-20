from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from polls.models import Question, Choice


# Create your views here.
def index(request):
    # 切片的语法是： list[start:end] 省略start表示以0开始，省略end表示到列表的结尾。注意，区间是左闭右开的！
    # 也就是说[1:4]会截取列表的索引为1/2/3的3个元素，不会截取索引为4的元素。分片不会修改原有的列表，
    # 可以将结果保存到新的变量，因此切片也是一种安全操作，常被用来复制一个列表，例如newlist = lis[:]。
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 用 ，拼接字符串
    # for循环简写：[ 对i的操作 for i in 列表 ]
    output = '，'.join([q.question_text for q in lastest_question_list])
    # return HttpResponse("这里是liujiangblog.com的投票站点: %s" % output)
    return HttpResponse(request, 'index.html')


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


def detail(requst, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question is not exist!!!!!")

    question = get_object_or_404(Question, pk=question_id)
    return render(requst, 'polls/detail.html', {'question': question})


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice. "})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # HttpResponseRedirect需要一个参数：重定向的URL。
        # 这里有一个建议，当你成功处理POST数据后，应当保持一个良好的习惯，始终返回一个HttpResponseRedirect。这不仅仅是对Django而言，它是一个良好的WEB开发习惯。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
