from django.contrib import admin
from .models import TuneType, Key, Tune, Composer, Meter, UnitNoteLength, BPM, YoutubePlaythrough
from .models import ABCTune, ABCTunePiece


@admin.register(TuneType)
class TuneTypeAdmin(admin.ModelAdmin):
    ordering = ("tune_type_char",)
    list_filter = ("tune_type_char",)
    list_display = ("tune_type_char",)


@admin.register(Tune)
class TuneAdmin(admin.ModelAdmin):
    ordering = ("name",)
    search_fields = ("name",)
    list_filter = ("tune_type__tune_type_char",)
    list_display = ("name", "tune_type", "composer")


@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    ordering = ("key_type_char",)
    list_filter = ("key_type_char",)
    list_display = ("key_type_char",)


@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    ordering = ('meter_type_char',)


@admin.register(UnitNoteLength)
class UnitNoteLengthAdmin(admin.ModelAdmin):
    ordering = ('unit_note_length',)


@admin.register(BPM)
class BPMAdmin(admin.ModelAdmin):
    ordering = ('bpm',)


@admin.register(Composer)
class ComposerAdmin(admin.ModelAdmin):
    ordering = ("name",)


@admin.register(ABCTunePiece)
class ABCTunePieceAdmin(admin.ModelAdmin):
    ordering = ("abc_tune", "part_order")


class ABCTunePieceInline(admin.TabularInline):
    model = ABCTunePiece
    extra = 0
    show_change_link = True


@admin.register(ABCTune)
class ABCTextAdmin(admin.ModelAdmin):
    ordering = ("tune",)
    list_filter = ("key",)
    inlines = [ABCTunePieceInline]

@admin.register(YoutubePlaythrough)
class YoutubePlaythroughAdmin(admin.ModelAdmin):
    ordering = ("date_recorded",)
    list_display = ("date_recorded", "tune", "title")
