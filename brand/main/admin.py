from django.contrib import admin
from .models import Services,About,Team,Clients,Portfolio,PortfolioFilling,Contact
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("id","title","description","icon_class","sort")
    list_editable = ("title","description","icon_class","sort") 
    list_filter = ("is_visible",)
    search_fields = ("title",)



@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("photo_src_tag","date_heading","subheading","description","sort")
    list_editable = ("subheading","description","sort")
    
    search_fields = ("date_heading",)

    def photo_src_tag(self,obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")
    
    photo_src_tag.short_description = "About photo"


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("photo_src_tag","name","title","social_media_links_preview","sort")
    list_editable = ("title","sort")
    search_fields = ('name', 'title')
    list_filter = ('title',)
    

    def photo_src_tag(self,obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")
    
    photo_src_tag.short_description = "Team photo"


    def social_media_links_preview(self, obj):
        links = []
        for platform, url in obj.social_media_links.items():
            links.append('<a href="%s"><i class="fa fa-%s"></i></a>' % (url, platform))
        return ', '.join(links)
    

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'url','is_visible')
    list_editable = ('name','url','is_visible')
    search_fields = ('name',)

    def photo_src_tag(self,obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50 height=50>")
    

# @admin.register(Portfolio)
# class PortfolioAdmin(admin.ModelAdmin):
#      list_display = ( "photo_src_tag","photo_src_tag2","title", "subheading","date","client","category")
#      list_editable = ('title',"subheading","date","client","category")
#      search_fields = ('title',)
#      list_filter = ('is_visible',)


#      def photo_src_tag(self,obj):
#         if obj.image_title:
#             return mark_safe(f"<img src='{obj.image_title.url}' width=50 height=50>")
    
#      def photo_src_tag2(self,obj):
#         if obj.image_full:
#             return mark_safe(f"<img src='{obj.image_full.url}' width=50 height=50>")


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
     list_display = ( "photo_src_tag","title", "subheading")
     list_editable = ('title',"subheading")
     search_fields = ('title',)
     list_filter = ('is_visible',)


     def photo_src_tag(self,obj):
        if obj.image_title:
            return mark_safe(f"<img src='{obj.image_title.url}' width=50 height=50>")
    
     


@admin.register(PortfolioFilling)
class PortfolioFillingAdmin(admin.ModelAdmin):
    list_display = ( "photo_src_tag","title", "subheading","date","client","category")
    list_editable = ('title',"subheading","date","client","category")
    search_fields = ('title',"date","client","category")

    def photo_src_tag(self,obj):
            if obj.image_full:
                return mark_safe(f"<img src='{obj.image_full.url}' width=50 height=50>")
            

admin.site.register(Contact)
        
