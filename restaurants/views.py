from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        'my_list': [
            {
                "restaurant_name":"cheese cake factory",
                "food_type":"international"
            },
            {
                "restaurant_name":"nan",
                "food_type":"indian"
            },
            {
                "restaurant_name":"krispy",
                "food_type":"sweet"
            }
        ]


    }

   
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        'my_object':
        	{
                "restaurant_name":"cheese cake factory",
                "food_type":"international"
            }
        
            
     
    }
    return render(request, 'detail.html', context)
