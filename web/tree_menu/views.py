from django.shortcuts import render


def first_menu(request):
    return render(
        request,
        "tree_menu/base.html",
        {"menu_name": "second"}
    )
