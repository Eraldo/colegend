from django.views.generic import TemplateView

__author__ = 'Eraldo Energy'


class AboutView(TemplateView):
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reasons'] = [
            {
                'npc': 'bear',
                'text': "I admit it - I often act impulsively! A big cake on the table? Well - I’ll eat it of course, no use in just looking at it! But I might get into troubles after… coLegend helps me to connect more with my needs and to take care of myself more consciously. I already tried sharing my impulses with others, hear their view on it - they even gave me input on how to try out alternative ways of dealing with my impulsivity. So I started to reflect on how I treat myself and now I have the option of changing things I don’t like yet and celebrating things I already do like.",
            },
            {
                'npc': 'dolphin',
                'text': "Guess what…. I DON’T CARE whether you like to join or not. You don’t need a reason - just do it or leave it. I LIKE IT and that’s more than enough for me :). It just feels good having a space to be accepted and celebrated for who I am with the whole package that comes along with it ;-)",
            },
            {
                'npc': 'tiger',
                'text': "coLegend represents a win-win situation for me - perfect for my taste! I pay a pretty low fee once a month and can use everything I like on the platform! So it’s up to me how much I get out of it - I can use it as often and as long as I want! Basically just like a personal development flat-rate! Love it *puuurrrr*",
            },
            {
                'npc': 'monkey',
                'text': "I’m so glad that coLegend finally is a platform that goes beyond the superficial surface! I can connect deeply with my fellow legends in a secure place where we can be honest and open with and can find out so much about each other as we can share our deepest feelings and thoughts! It feels good to have people around that understand me and are there for me - people that I can support just as well by being myself.",
            },
            {
                'npc': 'parrot',
                'text': "I’ve always said that once you’re not alone you can basically accomplish everything! And in coLegend I’m finally proven right! Here I can connect with others that want the exact same thing as I want: Help each other to get what we want! And the more the merrier - so what are you waiting for? Join!!!!",
            },
            {
                'npc': 'eagle',
                'text': "In the hectic everyday life it often happens that one does not spend time on reflecting on what they’re doing - you can ask yourself: Are you still on the path you wanted to go in the first place? On coLegend we pay attention to what truly motivates or hinders us on our way to greatness. You just have to dare to open your eyes to your inner truth.",
            },
            {
                'npc': 'phoenix',
                'text': "We’re already waiting for you - there’s much to be done...",
            },
        ]
        return context
