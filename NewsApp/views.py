from django.shortcuts import render

# Create your views here.


def breaking_news(request):
    return render(request, 'NewsApp/result.html')


def movie_news(request):
    news1 = 'In Telgu DevDas movie is not Good'
    news2 = 'Salman Updating Minimum 100 crores Guarantee for his Movies'
    news3 = 'Sonali slowly getting curing'
    news4 = 'Amitabh Bachchan next movie is Thugs of Hindustan'
    news5 = 'Salman and Katrina going to marry soon'
    my_dict = {'news1': news1, 'news2': news2, 'news3': news3, 'news4': news4, 'news5': news5}
    return render(request, 'NewsApp/result1.html', my_dict)

def sports_News(request):
    news1 = 'Virat Kohli became father of one child.'
    news2 = 'Seraj wepen at the time of singing national anthem.'
    news3 = 'M.S Dhoni become a farmer after quiting Cricket.'
    news4 = 'India more chance to win next cricket world cup.'
    news5 = 'Sania Nehwal will marry next month'
    my_dict = {'news1': news1, 'news2': news2, 'news3': news3, 'news4': news4, 'news5': news5}
    return render(request, 'NewsApp/sports.html', my_dict)