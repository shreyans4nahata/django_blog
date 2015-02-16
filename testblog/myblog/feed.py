from django.contrib.syndication.views import Feed
from .models import entry
class latest(Feed):
	title = "Shreyans Blog"
	link = "/feed/"
	description = "Latest Posts on my blog"

	def items(self):
		return entry.objects.published()[:5]
		