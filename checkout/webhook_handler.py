from django.http import HttpResponse


class StripeWH_Handler:
    """ handle stripe webhooks""" 

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ handle webhook events i.e normal/unknown or non expected"""
        return HttpResponse(
            content=f'unhandled webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ handle payment_intent_succeeded webhook """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """ handle payment_intent_failed webhook """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
