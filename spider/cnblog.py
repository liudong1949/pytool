#! /usr/bin/env python
# coding:utf-8
import urllib,urllib2,cookielib
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent,'Referer':'https://passport.cnblogs.com/login.aspx?ReturnUrl=http://www.cnblogs.com/yuliyang/admin/EditPosts.aspx',
           'Host':'passport.cnblogs.com',
           }
params={'tbUserName':'BeginMan',
                'tbPassword':'1991fang',
                "__EVENTVALIDATION":"/wEdAAUyDI6H/s9f+ZALqNAA4PyUhI6Xi65hwcQ8/QoQCF8JIahXufbhIqPmwKf992GTkd0wq1PKp6+/1yNGng6H71Uxop4oRunf14dz2Zt2+QKDEIYpifFQj3yQiLk3eeHVQqcjiaAP",
                "__VIEWSTATE":"/wEPDwULLTE1MzYzODg2NzZkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQtjaGtSZW1lbWJlcm1QYDyKKI9af4b67Mzq2xFaL9Bt",
                "btnLogin":"登  录",
                "txtReturnUrl":"http://home.cnblogs.com/"}
print 'login......'
params=urllib.urlencode(params)
#设置cookie
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
request2=urllib2.Request('https://passport.cnblogs.com/login.aspx',params)
response2 =  opener.open(request2)#post 数据
#print response2.read()
print "log success"
params2={
    '__VIEWSTATE':'/wEPDwUKLTg5MDEzODY0MQ8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBFgJmD2QWBgIGDxYCHgRUZXh0BUo8bGluayByZWw9InN0eWxlc2hlZXQiIHR5cGU9InRleHQvY3NzIiBocmVmPSIvY3NzL2FkbWluLmNzcz9pZD0yMDE0MDExMCIvPmQCCA8WAh8BBZ0BPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiIHNyYz0iL3NjcmlwdC9qcXVlcnkuY25ibG9ncy50aGlja2JveC5qcyI+PC9zY3JpcHQ+CjxzY3JpcHQgdHlwZT0idGV4dC9qYXZhc2NyaXB0IiBzcmM9Ii9zY3JpcHQvYWRtaW4uanM/aWQ9MjAxNDAxMTAiPjwvc2NyaXB0PmQCCg9kFgICAQ9kFhYCAQ8PFgIeC05hdmlnYXRlVXJsBSBodHRwOi8vd3d3LmNuYmxvZ3MuY29tL0JlZ2luTWFuL2RkAgMPDxYGHgZUYXJnZXRlHwIFIGh0dHA6Ly93d3cuY25ibG9ncy5jb20vQmVnaW5NYW4vHwEFCEJlZ2luTWFuZGQCBQ8PFgQfAgUXaHR0cDovL3d3dy5jbmJsb2dzLmNvbS8eCEltYWdlVXJsBS5odHRwOi8vc3RhdGljLmNuYmxvZ3MuY29tL2ltYWdlcy9hZG1pbmxvZ28uZ2lmZGQCCQ8WAh4HVmlzaWJsZWhkAg8PFgIfBWdkAiMPZBYCAgEPZBYMAgEPDxYGHglDb2xsYXBzZWRnHgtDb2xsYXBzaWJsZWcfBWhkZAICD2QWBGYPZBYCZg8PFgIfAQUM5re75Yqg6ZqP56yUZGQCAQ9kFhACAQ8PFgQfAmUfBWhkZAIDDw9kFgIeCW9ua2V5ZG93bgUVdGl0bGVfa2V5ZG93bihldmVudCk7ZAIFDxYCHwEFEyhNYXJrZG93bue8lui+keWZqClkAgkPZBYCAgEPZBYIAgEPZBYCAgEPZBYCAgEPEA8WBh4ORGF0YVZhbHVlRmllbGQFCkNhdGVnb3J5SUQeDURhdGFUZXh0RmllbGQFBVRpdGxlHgtfIURhdGFCb3VuZGdkEBUQFuOAiumUi+WIqeeahGpxdWVyeTLjgIsSZGphbmdv5a6Y572R5bCP6IqCDERqYW5nb+WFpemXqANHaXQKSmF2YVNjcmlwdAZq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Y2tsQ2F0ZWdvcmllcyQwBTRFZGl0b3IkRWRpdCRBUE9wdGlvbnMkQWR2YW5jZWRwYW5lbDEkY2tsQ2F0ZWdvcmllcyQxBTRFZGl0b3IkRWRpdCRBUE9wdGlvbnMkQWR2YW5jZWRwYW5lbDEkY2tsQ2F0ZWdvcmllcyQyBTRFZGl0b3IkRWRpdCRBUE9wdGlvbnMkQWR2YW5jZWRwYW5lbDEkY2tsQ2F0ZWdvcmllcyQzBTRFZGl0b3IkRWRpdCRBUE9wdGlvbnMkQWR2YW5jZWRwYW5lbDEkY2tsQ2F0ZWdvcmllcyQ0BTRFZGl0b3IkRWRpdCRBUE9wdGlvbnMkQWR2YW5jZWRwYW5lbDEkY2tsQ2F0ZWdvcmllcyQ1BTRFZGl0b3IkRWRpdCRBUE9wdGlvbnMkQWR2YW5jZWRwYW5lbDEkY2tsQ2F0ZWdvcmllcyQ2BTRFZGl0b3IkRWRpdCRBUE9wdGlvbnMkQWR2YW5jZWRwYW5lbDEkY2tsQ2F0ZWdvcmllcyQ3BTRFZGl0b3IkRWRpdCRBUE9wdGlvbnMkQWR2YW5jZWRwYW5lbDEkY2tsQ2F0ZWdvcmllcyQ4BTRFZGl0b3IkRWRpdCRBUE9wdGlvbnMkQWR2YW5jZWRwYW5lbDEkY2tsQ2F0ZWdvcmllcyQ5BTVFZGl0b3IkRWRpdCRBUE9wdGlvbnMkQWR2YW5jZWRwYW5lbDEkY2tsQ2F0ZWdvcmllcyQxMAU1RWRpdG9yJEVkaXQkQVBPcHRpb25zJEFkdmFuY2VkcGFuZWwxJGNrbENhdGVnb3JpZXMkMTEFNUVkaXRvciRFZGl0JEFQT3B0aW9ucyRBZHZhbmNlZHBhbmVsMSRja2xDYXRlZ29yaWVzJDEyBTVFZGl0b3IkRWRpdCRBUE9wdGlvbnMkQWR2YW5jZWRwYW5lbDEkY2tsQ2F0ZWdvcmllcyQxMwU1RWRpdG9yJEVkaXQkQVBPcHRpb25zJEFkdmFuY2VkcGFuZWwxJGNrbENhdGVnb3JpZXMkMTQFNUVkaXRvciRFZGl0JEFQT3B0aW9ucyRBZHZhbmNlZHBhbmVsMSRja2xDYXRlZ29yaWVzJDE1BTVFZGl0b3IkRWRpdCRBUE9wdGlvbnMkQWR2YW5jZWRwYW5lbDEkY2tsQ2F0ZWdvcmllcyQxNQUzRWRpdG9yJEVkaXQkQVBPcHRpb25zJEFQU2l0ZUhvbWUkY2hrRGlzcGxheUhvbWVQYWdlBTBFZGl0b3IkRWRpdCRBUE9wdGlvbnMkQVBTaXRlSG9tZSRjYkhvbWVDYW5kaWRhdGUFNkVkaXRvciRFZGl0JEFQT3B0aW9ucyRBUFNpdGVIb21lJGNiSXNQdWJsaXNoVG9TaXRlSG9tZQUhRWRpdG9yJEVkaXQkQWR2YW5jZWQkY2tiUHVibGlzaGVkBSBFZGl0b3IkRWRpdCRBZHZhbmNlZCRjaGtDb21tZW50cwUwRWRpdG9yJEVkaXQkQWR2YW5jZWQkY2hrRGlzYWJsZUFub255bW91c0NvbW1lbnRzBSdFZGl0b3IkRWRpdCRBZHZhbmNlZCRjaGtNYWluU3luZGljYXRpb24FJUVkaXRvciRFZGl0JEFkdmFuY2VkJGNoa0Z1bGxUZXh0SW5Sc3MFHkVkaXRvciRFZGl0JEFkdmFuY2VkJGNoa1Bpbm5lZAUtRWRpdG9yJEVkaXQkQWR2YW5jZWQkY2hrSXNPbmx5Rm9yUmVnaXN0ZXJVc2Vy',
                'Editor$Edit$txbTitle':'test3',#文章标题
                "Editor$Edit$EditorBody":"<p>33333333333333333333333</p>",#文章内容
                "Editor$Edit$APOptions$APSiteHome$chkDisplayHomePage":"on",
                "Editor$Edit$Advanced$ckbPublished":"on",
                "Editor$Edit$Advanced$chkComments":"on",
                "Editor$Edit$Advanced$chkMainSyndication":"on",
                "Editor$Edit$Advanced$txbEntryName":"",
                "Editor$Edit$Advanced$txbExcerpt":"",
                "Editor$Edit$Advanced$txbTag":"",
                "Editor$Edit$Advanced$tbEnryPassword":"",
                "Editor$Edit$lkbPost":"发布"}
params2=urllib.urlencode(params2)
print "start to write a new blog"
request3=opener.open("http://www.cnblogs.com/BeginMan/admin/EditPosts.aspx?opt=1",params2)#post数据
print "success write !"
#print request3.read()
# request3=urllib2.Request("https://www.cnblogs.com/yuliyang/admin/EditPosts.aspx")