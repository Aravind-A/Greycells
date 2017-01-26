from django.shortcuts import render,redirect
from django.db.models import F
from django.core.urlresolvers import reverse
from users.models import Participant
from .models import Question

# Create your views here.

def q_view(request,sluggy):
    if request.user.is_authenticated():
        p = Participant.objects.get(user=request.user)
        q = Question.objects.get(slug=sluggy)
        correct = -1
        if request.method == 'POST':
            ans = request.POST["answer"]
            qs = Participant.objects.all()
            
            if ans == q.answer:
                q.numsolved = F('numsolved') + 1
                q.save(update_fields = ['numsolved'])
                if p.level != 3:
                    key = Question.objects.get(level = p.level+1).slug
                else:
                    key = 'last'
                p.level = F('level') + 1
                p.save(update_fields = ['level'])
                for i,item in enumerate(qs):
                    item.rank = i + 1
                    item.save(update_fields = ['rank'])
                correct = 1
                if key == 'last':
                    return redirect(reverse('users:dashboard'))
                return redirect(reverse('questions:q_view', kwargs = { 'sluggy' : key }))
                
            else:
                p.points = F('points') + 0.25
                p.save(update_fields = ['points'])
                correct = 0
                for i,item in enumerate(qs):
                    item.rank = i + 1
                    item.save(update_fields = ['rank'])
                
            
        return render(request,"qview.html",{'p' : p,'correct' : correct,'q' : q })
            
            