from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import date

def trash_view(request):
  def odd_week():
    return ((date.today() - date(2012,1,1)).days / 7) % 2
  
  if odd_week():
    context = {
      'image': "green.png",
      'alt': "Happy green Earth",
      'text': "No trash this week! Only recyclables and yard refuse.",
    }
  else:
    context = {
      'image': "trash.png",
      'alt': "Don't be a pig!",
      'text': "This week is trash week; go forth and be wasteful.",
    }
  
  return render_to_response('trash/trash.html', context, RequestContext(request))