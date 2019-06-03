from devices.models import Job


def create_post_request_entry(controller_model, data_field_name):
    def create_request_entry_decorator(func):
        def wrapper(request):
            Job.objects.create(
                controller=controller_model.objects.get(id=request.POST.get('controller')),
                user=request.user,
                data=request.POST.get(data_field_name)
            )
            return func(request)
        return wrapper
    return create_request_entry_decorator
    


# def redirect_if_wrong_boardname(func):
#     def wrapper(request, board_id, board_name):
#         try:
#             board = Board.objects.get(pk=board_id)
#             if (board.name != board_name):
#                 return redirect('/boards/' + board.pk + '/' + board.name)
#             else:
#                 return func(request, board_id, board_name)
#         except:
#             return Http404('Board not found')
#     return wrapper