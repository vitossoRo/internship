from django import forms

from blog.models import BlogPost

class CreateBlogPostForm(forms.ModelForm):

	class Meta:
		model = BlogPost
		fields = ['title', 'body', 'image', 'price', 'SKU', 'enabled']



class UpdateBlogPostForm(forms.ModelForm):

	class Meta:
		model = BlogPost
		fields = ['title', 'body', 'image', 'price', 'SKU', 'enabled']

	def save(self, commit=True):
		blog_post = self.instance
		blog_post.title = self.cleaned_data['title']
		blog_post.body = self.cleaned_data['body']
		blog_post.price = self.cleaned_data['price']
		blog_post.SKU = self.cleaned_data['SKU']
		blog_post.enabled = self.cleaned_data['enabled']

		if self.cleaned_data['image']:
			blog_post.image = self.cleaned_data['image']

		if commit:
			blog_post.save()
		return blog_post
