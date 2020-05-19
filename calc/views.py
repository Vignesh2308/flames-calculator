from django.shortcuts import render
from calc.forms import Details


# Create your views here.

def home(request):
    form = Details()

    if request.method == 'POST':
        form = Details(request.POST)
        if form.is_valid():
            name1 = str(form.cleaned_data['first_name'])
            name2 = str(form.cleaned_data['partner_name'])
            name1_list = list(str(form.cleaned_data['first_name']).lower().replace(" ", ""))
            name2_list = list(str(form.cleaned_data['partner_name']).lower().replace(" ", ""))
            names = []
            for i in name1_list:
                if i not in name2_list:
                    names.append(i)
                else:
                    name2_list.remove(i)
            names.extend(name2_list)
            unique_letters = len(names)
            flames = ['F', 'L', 'A', 'M', 'E', 'S']

            while len(flames) > 1:
                length_of_flames = len(flames)
                index_value = (unique_letters % length_of_flames) - 1

                flames.remove(flames[index_value])
                if index_value != -1:
                    flames = (flames[index_value:]) + (flames[:index_value])

            message = {
                'F': name1.upper() + ' AND ' + name2.upper() + ' ARE FRIENDS',
                'L': name2.upper() + ' LOVES ' + name1.upper(),
                'A': name2.upper() + ' IS AFFECTIONATE TOWARDS ' + name1.upper(),
                'M': name1.upper() + ' AND ' + name2.upper() + ' WILL GET MARRIED',
                'E': name1.upper() + ' AND ' + name2.upper() + ' ARE ENEMIES',
                'S': name1.upper() + ' AND ' + name1.upper() + ' ARE LIKE BROTHERS AND SISTERS',
            }

            relationship = message.get(flames[0])
            context = {'status': relationship, 'form': form}
            return render(request, 'calc/form.html', context)

    return render(request, 'calc/form.html', context={'form': form})
