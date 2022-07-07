from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import Http404


def is_login(func):
	def _(request, *args, **kwargs):
		if request.user.is_authenticated:
			return func(request, *args, **kwargs)
		else:
			return redirect('users:login')
	
	return _


def index(request):
	return render(request, 'index.html')


@is_login
def topics(request):
	topics_ = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics': topics_}
	return render(request, 'topics.html', context=context)


@is_login
def new_topic(request):
	context = {'TopicForm': TopicForm()}
	if request.method == 'POST':
		f = TopicForm(data=request.POST)
		if f.is_valid():
			t = f.save(commit=False)
			t.owner = request.user
			t.save()
			return redirect('learning_logs:topics')
	
	return render(request, 'new_topic.html', context)


@is_login
def new_entry(request, topic_id):
	t = Topic.objects.get(id=topic_id)
	if request.user != t.owner:
		raise Http404
	if request.method != 'POST':
		form = EntryForm()
		context = {'form': form, 'topic_id': topic_id}
	else:
		e = Entry()
		e.topic = t
		form = EntryForm(instance=e, data=request.POST)
		context = {'form': form, 'topic_id': topic_id, 'topic': t}
		if form.is_valid():
			form.save()
			return redirect('learning_logs:topics')
	return render(request, 'new_entry.html', context)


@is_login
def open_topic(request, topic_id):
	t = Topic.objects.get(id=topic_id)
	if request.user != t.owner:
		raise Http404
	context = {'topic': t, 'entries': t.entry_set.all()}
	return render(request, 'open_topic.html', context)


@is_login
def edit_entry(request, entry_id):
	e = Entry.objects.get(id=entry_id)
	t = e.topic
	if request.user != t.owner:
		raise Http404
	if request.method != 'POST':
		form = EntryForm(instance=e)
	else:
		form = EntryForm(instance=e, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_logs:topics')
	context = {'topic': t, 'form': form, 'topic_id': entry_id}
	return render(request, 'edit_entry.html', context)


@is_login
def delete_topic(request, topic_id):
	t = Topic.objects.get(id=topic_id)
	if request.user != t.owner:
		raise Http404
	t.delete()
	return redirect('learning_logs:topics')


@is_login
def delete_entry(request, entry_id):
	e = Entry.objects.get(id=entry_id)
	t = e.topic
	if request.user != t.owner:
		raise Http404
	e.delete()
	return redirect('learning_logs:topics')
