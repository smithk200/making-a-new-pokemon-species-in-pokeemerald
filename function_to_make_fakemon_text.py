gen9mons = ['Fuecoco','Crocalor','Skeledirge']
cloverlist = ['Bacub','Urswine','Tricient','Tricillion', 'Clovenix','Inbitween','Geigh','Dragking']
def define_species(self):
    j = 906#change if needed
    print "For include/constants/species.h"
    print
    for i in self:
        j+=1
        print "#define SPECIES_"+i.upper()+"            "+str(j)
def graphics_h(self):
    print "For include/graphics.h"
    print
    for i in self:
        print """extern const u32 gMonFrontPic_"""+i+"""[];"""
    print
    for i in self:
        print """extern const u32 gMonBackPic_"""+i+"""[];"""
    print
    for i in self:
        print """extern const u32 gMonPalette_"""+i+"""[];"""
    print
    for i in self:
        print """extern const u32 gMonShinyPalette_"""+i+"""[];"""
    print
    for i in self:
        print """extern const u8 gMonIcon_"""+i+"""[];"""
    print
    for i in self:
        print """extern const u8 gMonFootprint_"""+i+"""[];"""

def link_graphics(self):
    print "For src/data/graphics/pokemon.h"
    print
    for i in self:
        print """const u32 gMonFrontPic_"""+i+"""[] = INCBIN_U32("graphics/pokemon/"""+i.lower()+"""/front.4bpp.lz");"""
    print
    for i in self:
        print """const u32 gMonBackPic_"""+i+"""[] = INCBIN_U32("graphics/pokemon/"""+i.lower()+"""/back.4bpp.lz");"""
    print
    for i in self:
        print """const u32 gMonPalette_"""+i+"""[] = INCBIN_U32("graphics/pokemon/"""+i.lower()+"""/normal.gbapal.lz");"""
    print
    for i in self:
        print """const u32 gMonShinyPalette_"""+i+"""[] = INCBIN_U32("graphics/pokemon/"""+i.lower()+"""/shiny.gbapal.lz");"""
    print
    for i in self:
        print """const u8 gMonIcon_"""+i+"""[] = INCBIN_U8("graphics/pokemon/"""+i.lower()+"""/icon.4bpp");"""
    print
    for i in self:
        print """const u8 gMonFootprint_"""+i+"""[] = INCBIN_U8("graphics/pokemon/"""+i.lower()+"""/footprint.1bpp");"""

def anim_front_pic(self):
    print "For  src/anim_mon_front_pics.c"
    print
    for i in self:
        print """const u32 gMonFrontPic_"""+i+"""[] = INCBIN_U32("graphics/pokemon/"""+i.lower()+"""/anim_front.4bpp.lz");"""

def pic_tables(self):
    print "For src/data/pokemon_graphics/front_pic_table.h"
    print
    for i in self:
        print """SPECIES_SPRITE("""+i.upper()+""", gMonFrontPic_"""+i+"""),"""
    print
    print
    print "For src/data/pokemon_graphics/back_pic_table.h"
    print
    for i in self:
        print """SPECIES_SPRITE("""+i.upper()+""", gMonBackPic_"""+i+"""),"""
    print
    print
    print "For src/data/pokemon_graphics/front_pic_coordinates.h"
    print
    for i in self:
        print """[SPECIES_"""+i.upper()+"""]                        = { .size = MON_COORDS_SIZE(64, 64), .y_offset = 0 },"""
    print
    print
    print "For src/data/pokemon_graphics/back_pic_coordinates.h"
    print
    for i in self:
        print """[SPECIES_"""+i.upper()+"""]        = { .size = MON_COORDS_SIZE(64, 64), .y_offset =  0 },"""
    print
    print
    print "For src/data/pokemon_graphics/footprint_table.h"
    print
    for i in self:
        print """[SPECIES_"""+i.upper()+"""] = gMonFootprint_"""+i+""","""
    print
    print "For src/data/pokemon_graphics/palette_table.h"
    print
    for i in self:
        print """SPECIES_PAL("""+i.upper()+""", gMonPalette_"""+i+"""),"""
    print
    print
    print "For src/data/pokemon_graphics/shiny_palette_table.h"
    print
    for i in self:
        print """SPECIES_SHINY_PAL("""+i.upper()+""", gMonShinyPalette_"""+i+"""),"""
    print
    print
    print "For src/pokemon_icon.c"
    print
    for i in self:
          print """[SPECIES_"""+i.upper()+"""] = gMonIcon_"""+i+""","""
    print
    for i in self:
        print """[SPECIES_"""+i.upper()+"""] = 0,"""
        
def cry(self):
    print "For sound/direct_sound_data.inc"
    print
    for i in self:
        print "Cry_"+i+"""::
	.incbin "sound/direct_sound_samples/cries/"""+i.lower()+'.bin"'
        print
        print "     .align 2"
    print
    print
    print "For sound/cry_tables.inc"
    print
    for i in self:
        print "cry Cry_"+i
    print
    for i in self:
        print "cry_reverse Cry_"+i

def miscellaneous(self):
    print "For src/data/pokemon/evolution.h"
    print
    for i in self:
        print "[SPECIES_"+i.upper()+"]              = {{EVO_LEVEL, 16, SPECIES_WARTORTLE}},"
    print
    print
    print "For src/data/easy_chat/easy_chat_words_by_letter.h"
    print
    for i in self:
        print "EC_POKEMON_NATIONAL("+i.upper()+"),"
    print
    print
    print "For src/data/pokemon_graphics/front_pic_anims.h"
    print
    for i in self:
        print """static const union AnimCmd *const sAnims_"""+i.upper()+"""[] =
{
    sAnim_GeneralFrame0,
    sAnim_"""+i.upper()+""",
};"""
    print
    for i in self:
        print """static const union AnimCmd sAnim_"""+i.upper()+"""[] =
{
    ANIMCMD_FRAME(0, 1),
    ANIMCMD_END,
};"""
    print
    for i in self:
        print "ANIM_CMD("+i.upper()+"),"
def base_stats(self): #Will make an advanced version later, that properly places all the stats in the correct place.
    print "For src/data/pokemon/base_stats.h"
    print
    for i in self:
            print "[SPECIES_"+i.upper()+"""] =
    {
        .baseHP        = 70,
        .baseAttack    = 55,
        .baseDefense   = 55,
        .baseSpeed     = 45,
        .baseSpAttack  = 80,
        .baseSpDefense = 60,
        .type1 = TYPE_ELECTRIC,
        .type2 = TYPE_ELECTRIC,
        .catchRate = 120,
        .expYield = 128,
        .evYield_SpAttack  = 2,
        .genderRatio = PERCENT_FEMALE(50),
        .eggCycles = 20,
        .friendship = 70,
        .growthRate = GROWTH_MEDIUM_SLOW,
        .eggGroup1 = EGG_GROUP_MONSTER,
        .eggGroup2 = EGG_GROUP_FIELD,
        .abilities = {ABILITY_STATIC, ABILITY_NONE, ABILITY_PLUS},
        .bodyColor = BODY_COLOR_PINK,
        .noFlip = FALSE,
    },"""
    print

def def_species(self):
    print "For  src/data/text/species_names.h"
    print
    for i in self:
        print '''[SPECIES_'''+i.upper()+'''] = _("'''+i+'''"),'''
    print
    print
    print "For  src/data/pokemon/pokedex_orders.h. Use in the functions gPokedexOrder_Alphabetical, gPokedexOrder_Weight, and gPokedexOrder_Height."
    print "Also, for  include/constants/pokedex.h."
    print
    for i in self:
        print '''NATIONAL_DEX_'''+i.upper()+''','''#You have to use this multiple times.
    print
    print
    print "For  src/pokemon.c"
    print
    for i in self:
        print '''SPECIES_TO_NATIONAL('''+i.upper()+'''),'''
    print
    for i in self:
        print "[SPECIES_"+i.upper()+" - 1]    = ANIM_H_SLIDE,"
    print
    print "For src/pokemon_animation.c"
    print
    for i in self:
        print "[SPECIES_"+i.upper()+"]     = BACK_ANIM_NONE,"
    print
    print "For  src/data/pokemon/pokedex_text.h"
    print
    for i in self:
        print 'const u8 g'+i+'PokedexText[] = _(\n    "This Pokemon appeared\\nin Pokemon Scarlet and Violet.");'
    print
    print
    print "For  src/data/pokemon/pokedex_entries.h"
    print
    for i in self:
        print """[NATIONAL_DEX_"""+i.upper()+'''] =
   {
        .categoryName = _("EditHere"),
        .height = 15,
        .weight = 330,
        .description = g'''+i+'''PokedexText,
        .pokemonScale = 100,
        .pokemonOffset = 0,
        .trainerScale = 290,
        .trainerOffset = 2,
    },'''

def learnsets(self):
    print "For src/data/pokemon/level_up_learnset_pointers.h"
    print
    for i in self:
        print """[SPECIES_"""+i.upper()+"""] = s"""+i+"""LevelUpLearnset,"""
    print
    print
    print "For src/data/pokemon/level_up_learnsets.h"
    print
    for i in self:
        print "static const struct LevelUpMove s"+i+"""LevelUpLearnset[] = {
    LEVEL_UP_MOVE( 1, MOVE_TACKLE),
    LEVEL_UP_MOVE( 1, MOVE_GROWL),
    LEVEL_UP_END
};"""
    print
    print
    print "For src/data/pokemon/teachable_learnsets.h"
    print
    for i in self:
        print """static const u16 s"""+i+"""TeachableLearnset[] = {
    MOVE_UNAVAILABLE,
};"""
    print
    print
    print "For src/data/pokemon/teachable_learnset_pointers.h"
    print
    for i in self:
        print "[SPECIES_"+i.upper()+"] = s"+i+"TeachableLearnset,"

def all_together(self):
    define_species(self)
    print
    graphics_h(self)
    print
    link_graphics(self)
    print
    pic_tables(self)
    print
    def_species(self)
    print
    learnsets(self)
    print
    cry(self)
    print
    base_stats(self)
    print
    miscellaneous(self)

all_together(cloverlist)
