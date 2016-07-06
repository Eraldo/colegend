from django.contrib.admin.templatetags.admin_static import static
from django.views.generic import TemplateView

from colegend.about.models import AboutPage
from colegend.home.views import PageMixin
from colegend.roles.models import Role

__author__ = 'Eraldo Energy'


class AboutView(PageMixin, TemplateView):
    page_class = AboutPage
    page_query_kwargs = {'slug': 'about'}
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context.get('page')
        if page:
            context['reasons'] = [
                {
                    'npc': 'bear',
                    'text': page.animal_1,
                    # 'text': "I admit it - I often act impulsively! A big cake on the table? Well - I’ll eat it of course, no use in just looking at it! But I might get into troubles after… coLegend helps me to connect more with my needs and to take care of myself more consciously. I already tried sharing my impulses with others, hear their view on it - they even gave me input on how to try out alternative ways of dealing with my impulsivity. So I started to reflect on how I treat myself and now I have the option of changing things I don’t like yet and celebrating things I already do like.",
                },
                {
                    'npc': 'dolphin',
                    'text': page.animal_2,
                    # 'text': "Guess what…. I DON’T CARE whether you like to join or not. You don’t need a reason - just do it or leave it. I LIKE IT and that’s more than enough for me :). It just feels good having a space to be accepted and celebrated for who I am with the whole package that comes along with it ;-)",
                },
                {
                    'npc': 'tiger',
                    'text': page.animal_3,
                    # 'text': "coLegend represents a win-win situation for me - perfect for my taste! I pay a pretty low fee once a month and can use everything I like on the platform! So it’s up to me how much I get out of it - I can use it as often and as long as I want! Basically just like a personal development flat-rate! Love it *puuurrrr*",
                },
                {
                    'npc': 'monkey',
                    'text': page.animal_4,
                    # 'text': "I’m so glad that coLegend finally is a platform that goes beyond the superficial surface! I can connect deeply with my fellow legends in a secure place where we can be honest and open with and can find out so much about each other as we can share our deepest feelings and thoughts! It feels good to have people around that understand me and are there for me - people that I can support just as well by being myself.",
                },
                {
                    'npc': 'parrot',
                    'text': page.animal_5,
                    # 'text': "I’ve always said that once you’re not alone you can basically accomplish everything! And in coLegend I’m finally proven right! Here I can connect with others that want the exact same thing as I want: Help each other to get what we want! And the more the merrier - so what are you waiting for? Join!!!!",
                },
                {
                    'npc': 'eagle',
                    'text': page.animal_6,
                    # 'text': "In the hectic everyday life it often happens that one does not spend time on reflecting on what they’re doing - you can ask yourself: Are you still on the path you wanted to go in the first place? On coLegend we pay attention to what truly motivates or hinders us on our way to greatness. You just have to dare to open your eyes to your inner truth.",
                },
                {
                    'npc': 'phoenix',
                    'text': page.animal_7,
                    # 'text': "We’re already waiting for you - there’s much to be done...",
                },

            ]
            context['feature_image'] = {
                'url': page.feature_image.get_rendition('max-1200x1200').url if page.feature_image else '',
                'name': page.feature_image,
            }
            for image_field in ['colegend_header_image', 'conscious_header_image', 'connected_header_image', 'continuous_header_image']:
                image = getattr(page, image_field)
                if image:
                    context[image_field] = {
                        'url': image.get_rendition('max-1200x1200').url,
                        'name': image,
                    }
        team_members = Role.objects.get(name__iexact='core manager').users.all()
        member_data = []
        anonymous_image = static('legends/images/anonymous.png')
        for user in team_members:
            avatar = user.get_avatar()
            image = avatar.url if avatar else ''
            social_accounts = user.socialaccount_set.all()
            social_accounts_data = []
            for account in social_accounts:
                social_accounts_data.append({
                    'url': account.get_profile_url(),
                    'icon': account.provider,
                })
            member_data.append(
                {
                    'image': image or anonymous_image,
                    'name': user.name,
                    'roles': user.roles.all(),
                    'social_accounts': social_accounts_data,
                    'url': user.get_absolute_url(),
                }
            )
        while len(member_data) < 4:
            member_data.append({
                'image': anonymous_image,
                'name': 'Your Name',
                'roles': ['your chosen roles'],
            })
        context['team_members'] = member_data
        return context
