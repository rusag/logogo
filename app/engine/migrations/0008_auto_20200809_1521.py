# Generated by Django 3.0.7 on 2020-08-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0007_auto_20200809_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='svg_post',
            name='slogan',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='svg_post',
            name='color',
            field=models.CharField(choices=[('#0048BA', 'Absolute Zero'), ('#B0BF1A', 'Acid Green'), ('#7CB9E8', 'Aero'), ('#C9FFE5', 'Aero Blue'), ('#B284BE', 'African Violet'), ('#5D8AA8', 'Air Force Blue (RAF)'), ('#00308F', 'Air Force Blue (USAF)'), ('#72A0C1', 'Air Superiority Blue'), ('#AF002A', 'Alabama Crimson'), ('#F2F0E6', 'Alabaster'), ('#F0F8FF', 'Alice Blue'), ('#84DE02', 'Alien Armpit'), ('#E32636', 'Alizarin Crimson'), ('#C46210', 'Alloy Orange'), ('#EFDECD', 'Almond'), ('#E52B50', 'Amaranth'), ('#9F2B68', 'Amaranth Deep Purple'), ('#F19CBB', 'Amaranth Pink'), ('#AB274F', 'Amaranth Purple'), ('#D3212D', 'Amaranth Red'), ('#3B7A57', 'Amazon Store'), ('#00C4B0', 'Amazonite'), ('#FFBF00', 'Amber'), ('#FF7E00', 'Amber (SAE/ECE)'), ('#FF033E', 'American Rose'), ('#9966CC', 'Amethyst'), ('#A4C639', 'Android Green'), ('#F2F3F4', 'Anti-Flash White'), ('#CD9575', 'Antique Brass'), ('#665D1E', 'Antique Bronze'), ('#915C83', 'Antique Fuchsia'), ('#841B2D', 'Antique Ruby'), ('#FAEBD7', 'Antique White'), ('#008000', 'Ao (English)'), ('#8DB600', 'Apple Green'), ('#FBCEB1', 'Apricot'), ('#00FFFF', 'Aqua'), ('#7FFFD4', 'Aquamarine'), ('#D0FF14', 'Arctic Lime'), ('#4B5320', 'Army Green'), ('#3B444B', 'Arsenic'), ('#8F9779', 'Artichoke'), ('#E9D66B', 'Arylide Yellow'), ('#B2BEB5', 'Ash Gray'), ('#87A96B', 'Asparagus'), ('#FF9966', 'Atomic Tangerine'), ('#A52A2A', 'Auburn'), ('#FDEE00', 'Aureolin'), ('#6E7F80', 'AuroMetalSaurus'), ('#568203', 'Avocado'), ('#FF2052', 'Awesome'), ('#C39953', 'Aztec Gold'), ('#007FFF', 'Azure'), ('#F0FFFF', 'Azure (Web Color)'), ('#F0FFFF', 'Azure Mist'), ('#DBE9F4', 'Azureish White'), ('#89CFF0', 'Baby Blue'), ('#A1CAF1', 'Baby Blue Eyes'), ('#F4C2C2', 'Baby Pink'), ('#FEFEFA', 'Baby Powder'), ('#FF91AF', 'Baker-Miller Pink'), ('#21ABCD', 'Ball Blue'), ('#FAE7B5', 'Banana Mania'), ('#FFE135', 'Banana Yellow'), ('#006A4E', 'Bangladesh Green'), ('#E0218A', 'Barbie Pink'), ('#7C0A02', 'Barn Red'), ('#1DACD6', 'Battery Charged Blue'), ('#848482', 'Battleship Grey'), ('#98777B', 'Bazaar'), ('#BCD4E6', 'Beau Blue'), ('#9F8170', 'Beaver'), ('#FA6E79', 'Begonia'), ('#F5F5DC', 'Beige'), ('#2E5894', "B'dazzled Blue"), ('#9C2542', "Big Dip O'ruby"), ('#E88E5A', 'Big Foot Feet'), ('#FFE4C4', 'Bisque'), ('#3D2B1F', 'Bistre'), ('#967117', 'Bistre Brown'), ('#CAE00D', 'Bitter Lemon'), ('#BFFF00', 'Bitter Lime'), ('#FE6F5E', 'Bittersweet'), ('#BF4F51', 'Bittersweet Shimmer'), ('#000000', 'Black'), ('#3D0C02', 'Black Bean'), ('#54626F', 'Black Coral'), ('#253529', 'Black Leather Jacket'), ('#3B3C36', 'Black Olive'), ('#BFAFB2', 'Black Shadows'), ('#FFEBCD', 'Blanched Almond'), ('#A57164', 'Blast-Off Bronze'), ('#318CE7', 'Bleu De France'), ('#ACE5EE', 'Blizzard Blue'), ('#FAF0BE', 'Blond'), ('#0000FF', 'Blue'), ('#1F75FE', 'Blue (Crayola)'), ('#0093AF', 'Blue (Munsell)'), ('#0087BD', 'Blue (NCS)'), ('#0018A8', 'Blue (Pantone)'), ('#333399', 'Blue (Pigment)'), ('#0247FE', 'Blue (RYB)'), ('#A2A2D0', 'Blue Bell'), ('#00B9FB', 'Blue Bolt'), ('#6699CC', 'Blue-Gray'), ('#0D98BA', 'Blue-Green'), ('#5DADEC', 'Blue Jeans'), ('#ACE5EE', 'Blue Lagoon'), ('#553592', 'Blue-Magenta Violet'), ('#126180', 'Blue Sapphire'), ('#8A2BE2', 'Blue-Violet'), ('#5072A7', 'Blue Yonder'), ('#4F86F7', 'Blueberry'), ('#1C1CF0', 'Bluebonnet'), ('#DE5D83', 'Blush'), ('#79443B', 'Bole'), ('#0095B6', 'Bondi Blue'), ('#E3DAC9', 'Bone'), ('#DDE26A', 'Booger Buster'), ('#CC0000', 'Boston University Red'), ('#006A4E', 'Bottle Green'), ('#873260', 'Boysenberry'), ('#0070FF', 'Brandeis Blue'), ('#B5A642', 'Brass'), ('#CB4154', 'Brick Red'), ('#1DACD6', 'Bright Cerulean'), ('#66FF00', 'Bright Green'), ('#BF94E4', 'Bright Lavender'), ('#D891EF', 'Bright Lilac'), ('#C32148', 'Bright Maroon'), ('#1974D2', 'Bright Navy Blue'), ('#FF007F', 'Bright Pink'), ('#08E8DE', 'Bright Turquoise'), ('#D19FE8', 'Bright Ube'), ('#FFAA1D', 'Bright Yellow (Crayola)'), ('#3399FF', 'Brilliant Azure'), ('#F4BBFF', 'Brilliant Lavender'), ('#FF55A3', 'Brilliant Rose'), ('#FB607F', 'Brink Pink'), ('#004225', 'British Racing Green'), ('#CD7F32', 'Bronze'), ('#737000', 'Bronze Yellow'), ('#964B00', 'Brown (Traditional)'), ('#A52A2A', 'Brown (Web)'), ('#6B4423', 'Brown-Nose'), ('#AF6E4D', 'Brown Sugar'), ('#cc9966', 'Brown Yellow'), ('#1B4D3E', 'Brunswick Green'), ('#FFC1CC', 'Bubble Gum'), ('#E7FEFF', 'Bubbles'), ('#7BB661', 'Bud Green'), ('#F0DC82', 'Buff'), ('#480607', 'Bulgarian Rose'), ('#800020', 'Burgundy'), ('#DEB887', 'Burlywood'), ('#A17A74', 'Burnished Brown'), ('#CC5500', 'Burnt Orange'), ('#E97451', 'Burnt Sienna'), ('#8A3324', 'Burnt Umber'), ('#24A0ED', 'Button Blue'), ('#BD33A4', 'Byzantine'), ('#702963', 'Byzantium'), ('#536872', 'Cadet'), ('#5F9EA0', 'Cadet Blue'), ('#91A3B0', 'Cadet Grey'), ('#006B3C', 'Cadmium Green'), ('#ED872D', 'Cadmium Orange'), ('#E30022', 'Cadmium Red'), ('#FFF600', 'Cadmium Yellow'), ('#A67B5B', 'Cafe Au Lait'), ('#4B3621', 'Cafe Noir'), ('#1E4D2B', 'Cal Poly Pomona Green'), ('#A3C1AD', 'Cambridge Blue'), ('#C19A6B', 'Camel'), ('#EFBBCC', 'Cameo Pink'), ('#78866B', 'Camouflage Green'), ('#FFFF99', 'Canary'), ('#FFEF00', 'Canary Yellow'), ('#FF0800', 'Candy Apple Red'), ('#E4717A', 'Candy Pink'), ('#00BFFF', 'Capri'), ('#592720', 'Caput Mortuum'), ('#C41E3A', 'Cardinal'), ('#00CC99', 'Caribbean Green'), ('#960018', 'Carmine'), ('#D70040', 'Carmine (M&P)'), ('#EB4C42', 'Carmine Pink'), ('#FF0038', 'Carmine Red'), ('#FFA6C9', 'Carnation Pink'), ('#B31B1B', 'Carnelian'), ('#56A0D3', 'Carolina Blue'), ('#ED9121', 'Carrot Orange'), ('#00563F', 'Castleton Green'), ('#062A78', 'Catalina Blue'), ('#703642', 'Catawba'), ('#C95A49', 'Cedar Chest'), ('#92A1CF', 'Ceil'), ('#ACE1AF', 'Celadon'), ('#007BA7', 'Celadon Blue'), ('#2F847C', 'Celadon Green'), ('#B2FFFF', 'Celeste'), ('#4997D0', 'Celestial Blue'), ('#DE3163', 'Cerise'), ('#EC3B83', 'Cerise Pink'), ('#007BA7', 'Cerulean'), ('#2A52BE', 'Cerulean Blue'), ('#6D9BC3', 'Cerulean Frost'), ('#007AA5', 'CG Blue'), ('#E03C31', 'CG Red'), ('#A0785A', 'Chamoisee'), ('#F7E7CE', 'Champagne'), ('#F1DDCF', 'Champagne Pink'), ('#36454F', 'Charcoal'), ('#232B2B', 'Charleston Green'), ('#E68FAC', 'Charm Pink'), ('#DFFF00', 'Chartreuse (Traditional)'), ('#7FFF00', 'Chartreuse (Web)'), ('#DE3163', 'Cherry'), ('#FFB7C5', 'Cherry Blossom Pink'), ('#954535', 'Chestnut'), ('#DE6FA1', 'China Pink'), ('#A8516E', 'China Rose'), ('#AA381E', 'Chinese Red'), ('#856088', 'Chinese Violet'), ('#4AFF00', 'Chlorophyll Green'), ('#7B3F00', 'Chocolate (Traditional)'), ('#D2691E', 'Chocolate (Web)'), ('#FFA700', 'Chrome Yellow'), ('#98817B', 'Cinereous'), ('#E34234', 'Cinnabar'), ('#D2691E', 'Cinnamon'), ('#CD607E', 'Cinnamon Satin'), ('#E4D00A', 'Citrine'), ('#9FA91F', 'Citron'), ('#7F1734', 'Claret'), ('#FBCCE7', 'Classic Rose'), ('#0047AB', 'Cobalt Blue'), ('#D2691E', 'Cocoa Brown'), ('#965A3E', 'Coconut'), ('#6F4E37', 'Coffee'), ('#C4D8E2', 'Columbia Blue'), ('#F88379', 'Congo Pink'), ('#002E63', 'Cool Black'), ('#8C92AC', 'Cool Grey'), ('#B87333', 'Copper'), ('#DA8A67', 'Copper (Crayola)'), ('#AD6F69', 'Copper Penny'), ('#CB6D51', 'Copper Red'), ('#996666', 'Copper Rose'), ('#FF3800', 'Coquelicot'), ('#FF7F50', 'Coral'), ('#F88379', 'Coral Pink'), ('#FF4040', 'Coral Red'), ('#FD7C6E', 'Coral Reef'), ('#893F45', 'Cordovan'), ('#FBEC5D', 'Corn'), ('#B31B1B', 'Cornell Red'), ('#6495ED', 'Cornflower Blue'), ('#FFF8DC', 'Cornsilk'), ('#2E2D88', 'Cosmic Cobalt'), ('#FFF8E7', 'Cosmic Latte'), ('#81613C', 'Coyote Brown'), ('#FFBCD9', 'Cotton Candy'), ('#FFFDD0', 'Cream'), ('#DC143C', 'Crimson'), ('#BE0032', 'Crimson Glory'), ('#990000', 'Crimson Red'), ('#F5F5F5', 'Cultured'), ('#00FFFF', 'Cyan'), ('#4E82B4', 'Cyan Azure'), ('#4682BF', 'Cyan-Blue Azure'), ('#28589C', 'Cyan Cobalt Blue'), ('#188BC2', 'Cyan Cornflower Blue'), ('#00B7EB', 'Cyan (Process)'), ('#58427C', 'Cyber Grape'), ('#FFD300', 'Cyber Yellow'), ('#F56FA1', 'Cyclamen'), ('#FFFF31', 'Daffodil'), ('#F0E130', 'Dandelion'), ('#00008B', 'Dark Blue'), ('#666699', 'Dark Blue-Gray'), ('#654321', 'Dark Brown'), ('#88654E', 'Dark Brown-Tangelo'), ('#5D3954', 'Dark Byzantium'), ('#A40000', 'Dark Candy Apple Red'), ('#08457E', 'Dark Cerulean'), ('#986960', 'Dark Chestnut'), ('#CD5B45', 'Dark Coral'), ('#008B8B', 'Dark Cyan'), ('#536878', 'Dark Electric Blue'), ('#B8860B', 'Dark Goldenrod'), ('#A9A9A9', 'Dark Gray (X11)'), ('#013220', 'Dark Green'), ('#006400', 'Dark Green (X11)'), ('#1F262A', 'Dark Gunmetal'), ('#00416A', 'Dark Imperial Blue'), ('#00147E', 'Dark Imperial Blue'), ('#1A2421', 'Dark Jungle Green'), ('#BDB76B', 'Dark Khaki'), ('#483C32', 'Dark Lava'), ('#734F96', 'Dark Lavender'), ('#534B4F', 'Dark Liver'), ('#543D37', 'Dark Liver (Horses)'), ('#8B008B', 'Dark Magenta'), ('#A9A9A9', 'Dark Medium Gray'), ('#003366', 'Dark Midnight Blue'), ('#4A5D23', 'Dark Moss Green'), ('#556B2F', 'Dark Olive Green'), ('#FF8C00', 'Dark Orange'), ('#9932CC', 'Dark Orchid'), ('#779ECB', 'Dark Pastel Blue'), ('#03C03C', 'Dark Pastel Green'), ('#966FD6', 'Dark Pastel Purple'), ('#C23B22', 'Dark Pastel Red'), ('#E75480', 'Dark Pink'), ('#003399', 'Dark Powder Blue'), ('#4F3A3C', 'Dark Puce'), ('#301934', 'Dark Purple'), ('#872657', 'Dark Raspberry'), ('#8B0000', 'Dark Red'), ('#E9967A', 'Dark Salmon'), ('#560319', 'Dark Scarlet'), ('#8FBC8F', 'Dark Sea Green'), ('#3C1414', 'Dark Sienna'), ('#8CBED6', 'Dark Sky Blue'), ('#483D8B', 'Dark Slate Blue'), ('#2F4F4F', 'Dark Slate Gray'), ('#177245', 'Dark Spring Green'), ('#918151', 'Dark Tan'), ('#FFA812', 'Dark Tangerine'), ('#483C32', 'Dark Taupe'), ('#CC4E5C', 'Dark Terra Cotta'), ('#00CED1', 'Dark Turquoise'), ('#D1BEA8', 'Dark Vanilla'), ('#9400D3', 'Dark Violet'), ('#9B870C', 'Dark Yellow'), ('#00703C', 'Dartmouth Green'), ('#555555', "Davy's Grey"), ('#D70A53', 'Debian Red'), ('#40826D', 'Deep Aquamarine'), ('#A9203E', 'Deep Carmine'), ('#EF3038', 'Deep Carmine Pink'), ('#E9692C', 'Deep Carrot Orange'), ('#DA3287', 'Deep Cerise'), ('#FAD6A5', 'Deep Champagne'), ('#B94E48', 'Deep Chestnut'), ('#704241', 'Deep Coffee'), ('#C154C1', 'Deep Fuchsia'), ('#056608', 'Deep Green'), ('#0E7C61', 'Deep Green-Cyan Turquoise'), ('#004B49', 'Deep Jungle Green'), ('#333366', 'Deep Koamaru'), ('#F5C71A', 'Deep Lemon'), ('#9955BB', 'Deep Lilac'), ('#CC00CC', 'Deep Magenta'), ('#820000', 'Deep Maroon'), ('#D473D4', 'Deep Mauve'), ('#355E3B', 'Deep Moss Green'), ('#FFCBA4', 'Deep Peach'), ('#FF1493', 'Deep Pink'), ('#A95C68', 'Deep Puce'), ('#850101', 'Deep Red'), ('#843F5B', 'Deep Ruby'), ('#FF9933', 'Deep Saffron'), ('#00BFFF', 'Deep Sky Blue'), ('#4A646C', 'Deep Space Sparkle'), ('#556B2F', 'Deep Spring Bud'), ('#7E5E60', 'Deep Taupe'), ('#66424D', 'Deep Tuscan Red'), ('#330066', 'Deep Violet'), ('#BA8759', 'Deer'), ('#1560BD', 'Denim'), ('#2243B6', 'Denim Blue'), ('#669999', 'Desaturated Cyan'), ('#C19A6B', 'Desert'), ('#EDC9AF', 'Desert Sand'), ('#EA3C53', 'Desire'), ('#B9F2FF', 'Diamond'), ('#696969', 'Dim Gray'), ('#C53151', 'Dingy Dungeon'), ('#9B7653', 'Dirt'), ('#1E90FF', 'Dodger Blue'), ('#FEF65B', 'Dodie Yellow'), ('#D71868', 'Dogwood Rose'), ('#85BB65', 'Dollar Bill'), ('#828E84', 'Dolphin Gray'), ('#664C28', 'Donkey Brown'), ('#967117', 'Drab'), ('#00009C', 'Duke Blue'), ('#E5CCC9', 'Dust Storm'), ('#EFDFBB', 'Dutch White'), ('#E1A95F', 'Earth Yellow'), ('#555D50', 'Ebony'), ('#C2B280', 'Ecru'), ('#1B1B1B', 'Eerie Black'), ('#614051', 'Eggplant'), ('#F0EAD6', 'Eggshell'), ('#1034A6', 'Egyptian Blue'), ('#7DF9FF', 'Electric Blue'), ('#FF003F', 'Electric Crimson'), ('#00FFFF', 'Electric Cyan'), ('#00FF00', 'Electric Green'), ('#6F00FF', 'Electric Indigo'), ('#F4BBFF', 'Electric Lavender'), ('#CCFF00', 'Electric Lime'), ('#BF00FF', 'Electric Purple'), ('#3F00FF', 'Electric Ultramarine'), ('#8F00FF', 'Electric Violet'), ('#FFFF33', 'Electric Yellow'), ('#50C878', 'Emerald'), ('#6C3082', 'Eminence'), ('#1B4D3E', 'English Green'), ('#B48395', 'English Lavender'), ('#AB4B52', 'English Red'), ('#CC474B', 'English Vermillion'), ('#563C5C', 'English Violet'), ('#96C8A2', 'Eton Blue'), ('#44D7A8', 'Eucalyptus'), ('#C19A6B', 'Fallow'), ('#801818', 'Falu Red'), ('#B53389', 'Fandango'), ('#DE5285', 'Fandango Pink'), ('#F400A1', 'Fashion Fuchsia'), ('#E5AA70', 'Fawn'), ('#4D5D53', 'Feldgrau'), ('#FDD5B1', 'Feldspar'), ('#4F7942', 'Fern Green'), ('#FF2800', 'Ferrari Red'), ('#6C541E', 'Field Drab'), ('#FF5470', 'Fiery Rose'), ('#B22222', 'Firebrick'), ('#CE2029', 'Fire Engine Red'), ('#E25822', 'Flame'), ('#FC8EAC', 'Flamingo Pink'), ('#6B4423', 'Flattery'), ('#F7E98E', 'Flavescent'), ('#EEDC82', 'Flax'), ('#A2006D', 'Flirt'), ('#FFFAF0', 'Floral White'), ('#FFBF00', 'Fluorescent Orange'), ('#FF1493', 'Fluorescent Pink'), ('#CCFF00', 'Fluorescent Yellow'), ('#FF004F', 'Folly'), ('#014421', 'Forest Green (Traditional)'), ('#228B22', 'Forest Green (Web)'), ('#A67B5B', 'French Beige'), ('#856D4D', 'French Bistre'), ('#0072BB', 'French Blue'), ('#FD3F92', 'French Fuchsia'), ('#86608E', 'French Lilac'), ('#9EFD38', 'French Lime'), ('#D473D4', 'French Mauve'), ('#FD6C9E', 'French Pink'), ('#811453', 'French Plum'), ('#4E1609', 'French Puce'), ('#C72C48', 'French Raspberry'), ('#F64A8A', 'French Rose'), ('#77B5FE', 'French Sky Blue'), ('#8806CE', 'French Violet'), ('#AC1E44', 'French Wine'), ('#A6E7FF', 'Fresh Air'), ('#E936A7', 'Frogert'), ('#FF00FF', 'Fuchsia'), ('#C154C1', 'Fuchsia (Crayola)'), ('#FF77FF', 'Fuchsia Pink'), ('#CC397B', 'Fuchsia Purple'), ('#C74375', 'Fuchsia Rose'), ('#E48400', 'Fulvous'), ('#CC6666', 'Fuzzy Wuzzy'), ('#DCDCDC', 'Gainsboro'), ('#E49B0F', 'Gamboge'), ('#996600', 'Gamboge Orange (Brown)'), ('#FFDF46', 'Gargoyle Gas'), ('#007F66', 'Generic Viridian'), ('#F8F8FF', 'Ghost White'), ('#B05C52', "Giant's Club"), ('#FE5A1D', 'Giants Orange'), ('#B06500', 'Ginger'), ('#6082B6', 'Glaucous'), ('#E6E8FA', 'Glitter'), ('#AB92B3', 'Glossy Grape'), ('#00AB66', 'GO Green'), ('#D4AF37', 'Gold (Metallic)'), ('#FFD700', 'Gold (Web) (Golden)'), ('#85754E', 'Gold Fusion'), ('#996515', 'Golden Brown'), ('#FCC200', 'Golden Poppy'), ('#FFDF00', 'Golden Yellow'), ('#DAA520', 'Goldenrod'), ('#676767', 'Granite Gray'), ('#A8E4A0', 'Granny Smith Apple'), ('#6F2DA8', 'Grape'), ('#808080', 'Gray'), ('#808080', 'Gray (HTML/CSS Gray)'), ('#BEBEBE', 'Gray (X11 Gray)'), ('#465945', 'Gray-Asparagus'), ('#8C92AC', 'Gray-Blue'), ('#00FF00', 'Green (Color Wheel) (X11 Green)'), ('#1CAC78', 'Green (Crayola)'), ('#008000', 'Green (HTML/CSS Color)'), ('#00A877', 'Green (Munsell)'), ('#009F6B', 'Green (NCS)'), ('#00AD43', 'Green (Pantone)'), ('#00A550', 'Green (Pigment)'), ('#66B032', 'Green (RYB)'), ('#1164B4', 'Green-Blue'), ('#009966', 'Green-Cyan'), ('#A7F432', 'Green Lizard'), ('#6EAEA1', 'Green Sheen'), ('#ADFF2F', 'Green-Yellow'), ('#885818', 'Grizzly'), ('#A99A86', 'Grullo'), ('#00FF7F', 'Guppie Green'), ('#2a3439', 'Gunmetal'), ('#663854', 'Halaya Ube'), ('#446CCF', 'Han Blue'), ('#5218FA', 'Han Purple'), ('#E9D66B', 'Hansa Yellow'), ('#3FFF00', 'Harlequin'), ('#46CB18', 'Harlequin Green'), ('#C90016', 'Harvard Crimson'), ('#DA9100', 'Harvest Gold'), ('#808000', 'Heart Gold'), ('#FF7A00', 'Heat Wave'), ('#960018', 'Heidelberg Red'), ('#DF73FF', 'Heliotrope'), ('#AA98A9', 'Heliotrope Gray'), ('#AA00BB', 'Heliotrope Magenta'), ('#F400A1', 'Hollywood Cerise'), ('#F0FFF0', 'Honeydew'), ('#006DB0', 'Honolulu Blue'), ('#49796B', "Hooker's Green"), ('#FF1DCE', 'Hot Magenta'), ('#FF69B4', 'Hot Pink'), ('#355E3B', 'Hunter Green'), ('#71A6D2', 'Iceberg'), ('#FCF75E', 'Icterine'), ('#71BC78', 'Iguana Green'), ('#319177', 'Illuminating Emerald'), ('#602F6B', 'Imperial'), ('#002395', 'Imperial Blue'), ('#66023C', 'Imperial Purple'), ('#ED2939', 'Imperial Red'), ('#B2EC5D', 'Inchworm'), ('#4C516D', 'Independence'), ('#138808', 'India Green'), ('#CD5C5C', 'Indian Red'), ('#E3A857', 'Indian Yellow'), ('#4B0082', 'Indigo'), ('#091F92', 'Indigo Dye'), ('#4B0082', 'Indigo (Web)'), ('#FF496C', 'Infra Red'), ('#360CCC', 'Interdimensional Blue'), ('#002FA7', 'International Klein Blue'), ('#FF4F00', 'International Orange (Aerospace)'), ('#BA160C', 'International Orange (Engineering)'), ('#C0362C', 'International Orange (Golden Gate Bridge)'), ('#5A4FCF', 'Iris'), ('#B3446C', 'Irresistible'), ('#F4F0EC', 'Isabelline'), ('#009000', 'Islamic Green'), ('#B2FFFF', 'Italian Sky Blue'), ('#FFFFF0', 'Ivory'), ('#00A86B', 'Jade'), ('#9D2933', 'Japanese Carmine'), ('#264348', 'Japanese Indigo'), ('#5B3256', 'Japanese Violet'), ('#F8DE7E', 'Jasmine'), ('#D73B3E', 'Jasper'), ('#A50B5E', 'Jazzberry Jam'), ('#DA614E', 'Jelly Bean'), ('#343434', 'Jet'), ('#F4CA16', 'Jonquil'), ('#8AB9F1', 'Jordy Blue'), ('#BDDA57', 'June Bud'), ('#29AB87', 'Jungle Green'), ('#4CBB17', 'Kelly Green'), ('#7C1C05', 'Kenyan Copper'), ('#3AB09E', 'Keppel'), ('#E8F48C', 'Key Lime'), ('#C3B091', 'Khaki (HTML/CSS) (Khaki)'), ('#F0E68C', 'Khaki (X11) (Light Khaki)'), ('#8EE53F', 'Kiwi'), ('#882D17', 'Kobe'), ('#E79FC4', 'Kobi'), ('#6B4423', 'Kobicha'), ('#354230', 'Kombu Green'), ('#512888', 'KSU Purple'), ('#E8000D', 'KU Crimson'), ('#087830', 'La Salle Green'), ('#D6CADD', 'Languid Lavender'), ('#26619C', 'Lapis Lazuli'), ('#FFFF66', 'Laser Lemon'), ('#A9BA9D', 'Laurel Green'), ('#CF1020', 'Lava'), ('#B57EDC', 'Lavender (Floral)'), ('#E6E6FA', 'Lavender (Web)'), ('#CCCCFF', 'Lavender Blue'), ('#FFF0F5', 'Lavender Blush'), ('#C4C3D0', 'Lavender Gray'), ('#9457EB', 'Lavender Indigo'), ('#EE82EE', 'Lavender Magenta'), ('#E6E6FA', 'Lavender Mist'), ('#FBAED2', 'Lavender Pink'), ('#967BB6', 'Lavender Purple'), ('#FBA0E3', 'Lavender Rose'), ('#7CFC00', 'Lawn Green'), ('#FFF700', 'Lemon'), ('#FFFACD', 'Lemon Chiffon'), ('#CCA01D', 'Lemon Curry'), ('#FDFF00', 'Lemon Glacier'), ('#E3FF00', 'Lemon Lime'), ('#F6EABE', 'Lemon Meringue'), ('#FFF44F', 'Lemon Yellow'), ('#1A1110', 'Licorice'), ('#545AA7', 'Liberty'), ('#FDD5B1', 'Light Apricot'), ('#ADD8E6', 'Light Blue'), ('#B5651D', 'Light Brown'), ('#E66771', 'Light Carmine Pink'), ('#88ACE0', 'Light Cobalt Blue'), ('#F08080', 'Light Coral'), ('#93CCEA', 'Light Cornflower Blue'), ('#F56991', 'Light Crimson'), ('#E0FFFF', 'Light Cyan'), ('#FF5CCD', 'Light Deep Pink'), ('#C8AD7F', 'Light French Beige'), ('#F984EF', 'Light Fuchsia Pink'), ('#FAFAD2', 'Light Goldenrod Yellow'), ('#D3D3D3', 'Light Gray'), ('#CC99CC', 'Light Grayish Magenta'), ('#90EE90', 'Light Green'), ('#FFB3DE', 'Light Hot Pink'), ('#F0E68C', 'Light Khaki'), ('#D39BCB', 'Light Medium Orchid'), ('#ADDFAD', 'Light Moss Green'), ('#FED8B1', 'Light Orange'), ('#E6A8D7', 'Light Orchid'), ('#B19CD9', 'Light Pastel Purple'), ('#FFB6C1', 'Light Pink'), ('#E97451', 'Light Red Ochre'), ('#FFA07A', 'Light Salmon'), ('#FF9999', 'Light Salmon Pink'), ('#20B2AA', 'Light Sea Green'), ('#87CEFA', 'Light Sky Blue'), ('#778899', 'Light Slate Gray'), ('#B0C4DE', 'Light Steel Blue'), ('#B38B6D', 'Light Taupe'), ('#E68FAC', 'Light Thulian Pink'), ('#FFFFE0', 'Light Yellow'), ('#C8A2C8', 'Lilac'), ('#AE98AA', 'Lilac Luster'), ('#BFFF00', 'Lime (Color Wheel)'), ('#00FF00', 'Lime (Web) (X11 Green)'), ('#32CD32', 'Lime Green'), ('#9DC209', 'Limerick'), ('#195905', 'Lincoln Green'), ('#FAF0E6', 'Linen'), ('#15F2FD', 'Loeen (Lopen) Look'), ('#DE6FA1', 'Liseran Purple'), ('#6CA0DC', 'Little Boy Blue'), ('#674C47', 'Liver'), ('#B86D29', 'Liver (Dogs)'), ('#6C2E1F', 'Liver (Organ)'), ('#987456', 'Liver Chestnut'), ('#6699CC', 'Livid'), ('#FFE4CD', 'Lumber'), ('#E62020', 'Lust'), ('#001C3D', 'Maastricht Blue'), ('#FFBD88', 'Macaroni And Cheese'), ('#CC3336', 'Madder Lake'), ('#FF00FF', 'Magenta'), ('#FF55A3', 'Magenta (Crayola)'), ('#CA1F7B', 'Magenta (Dye)'), ('#D0417E', 'Magenta (Pantone)'), ('#FF0090', 'Magenta (Process)'), ('#9F4576', 'Magenta Haze'), ('#CC338B', 'Magenta-Pink'), ('#AAF0D1', 'Magic Mint'), ('#FF4466', 'Magic Potion'), ('#F8F4FF', 'Magnolia'), ('#C04000', 'Mahogany'), ('#FBEC5D', 'Maize'), ('#6050DC', 'Majorelle Blue'), ('#0BDA51', 'Malachite'), ('#979AAA', 'Manatee'), ('#F37A48', 'Mandarin'), ('#FF8243', 'Mango Tango'), ('#74C365', 'Mantis'), ('#880085', 'Mardi Gras'), ('#EAA221', 'Marigold'), ('#C32148', 'Maroon (Crayola)'), ('#800000', 'Maroon (HTML/CSS)'), ('#B03060', 'Maroon (X11)'), ('#E0B0FF', 'Mauve'), ('#915F6D', 'Mauve Taupe'), ('#EF98AA', 'Mauvelous'), ('#47ABCC', 'Maximum Blue'), ('#30BFBF', 'Maximum Blue Green'), ('#ACACE6', 'Maximum Blue Purple'), ('#5E8C31', 'Maximum Green'), ('#D9E650', 'Maximum Green Yellow'), ('#733380', 'Maximum Purple'), ('#D92121', 'Maximum Red'), ('#A63A79', 'Maximum Red Purple'), ('#FAFA37', 'Maximum Yellow'), ('#F2BA49', 'Maximum Yellow Red'), ('#4C9141', 'May Green'), ('#73C2FB', 'Maya Blue'), ('#E5B73B', 'Meat Brown'), ('#66DDAA', 'Medium Aquamarine'), ('#0000CD', 'Medium Blue'), ('#E2062C', 'Medium Candy Apple Red'), ('#AF4035', 'Medium Carmine'), ('#F3E5AB', 'Medium Champagne'), ('#035096', 'Medium Electric Blue'), ('#1C352D', 'Medium Jungle Green'), ('#DDA0DD', 'Medium Lavender Magenta'), ('#BA55D3', 'Medium Orchid'), ('#0067A5', 'Medium Persian Blue'), ('#9370DB', 'Medium Purple'), ('#BB3385', 'Medium Red-Violet'), ('#AA4069', 'Medium Ruby'), ('#3CB371', 'Medium Sea Green'), ('#80DAEB', 'Medium Sky Blue'), ('#7B68EE', 'Medium Slate Blue'), ('#C9DC87', 'Medium Spring Bud'), ('#00FA9A', 'Medium Spring Green'), ('#674C47', 'Medium Taupe'), ('#48D1CC', 'Medium Turquoise'), ('#79443B', 'Medium Tuscan Red'), ('#D9603B', 'Medium Vermilion'), ('#C71585', 'Medium Violet-Red'), ('#F8B878', 'Mellow Apricot'), ('#F8DE7E', 'Mellow Yellow'), ('#FDBCB4', 'Melon'), ('#0A7E8C', 'Metallic Seaweed'), ('#9C7C38', 'Metallic Sunburst'), ('#E4007C', 'Mexican Pink'), ('#7ED4E6', 'Middle Blue'), ('#8DD9CC', 'Middle Blue Green'), ('#8B72BE', 'Middle Blue Purple'), ('#210837', 'Middle Red Purple'), ('#4D8C57', 'Middle Green'), ('#ACBF60', 'Middle Green Yellow'), ('#D982B5', 'Middle Purple'), ('#E58E73', 'Middle Red'), ('#A55353', 'Middle Red Purple'), ('#FFEB00', 'Middle Yellow'), ('#ECB176', 'Middle Yellow Red'), ('#702670', 'Midnight'), ('#191970', 'Midnight Blue'), ('#004953', 'Midnight Green (Eagle Green)'), ('#FFC40C', 'Mikado Yellow'), ('#FDFFF5', 'Milk'), ('#FFDAE9', 'Mimi Pink'), ('#E3F988', 'Mindaro'), ('#36747D', 'Ming'), ('#F5E050', 'Minion Yellow'), ('#3EB489', 'Mint'), ('#F5FFFA', 'Mint Cream'), ('#98FF98', 'Mint Green'), ('#BBB477', 'Misty Moss'), ('#FFE4E1', 'Misty Rose'), ('#FAEBD7', 'Moccasin'), ('#967117', 'Mode Beige'), ('#73A9C2', 'Moonstone Blue'), ('#AE0C00', 'Mordant Red 19'), ('#8DA399', 'Morning Blue'), ('#8A9A5B', 'Moss Green'), ('#30BA8F', 'Mountain Meadow'), ('#997A8D', 'Mountbatten Pink'), ('#18453B', 'MSU Green'), ('#306030', 'Mughal Green'), ('#C54B8C', 'Mulberry'), ('#828E84', "Mummy's Tomb"), ('#FFDB58', 'Mustard'), ('#317873', 'Myrtle Green'), ('#D65282', 'Mystic'), ('#AD4379', 'Mystic Maroon'), ('#F6ADC6', 'Nadeshiko Pink'), ('#2A8000', 'Napier Green'), ('#FADA5E', 'Naples Yellow'), ('#FFDEAD', 'Navajo White'), ('#000080', 'Navy'), ('#9457EB', 'Navy Purple'), ('#FFA343', 'Neon Carrot'), ('#FE4164', 'Neon Fuchsia'), ('#39FF14', 'Neon Green'), ('#214FC6', 'New Car'), ('#D7837F', 'New York Pink'), ('#727472', 'Nickel'), ('#A4DDED', 'Non-Photo Blue'), ('#059033', 'North Texas Green'), ('#E9FFDB', 'Nyanza'), ('#4F42B5', 'Ocean Blue'), ('#0077BE', 'Ocean Boat Blue'), ('#48BF91', 'Ocean Green'), ('#CC7722', 'Ochre'), ('#008000', 'Office Green'), ('#FD5240', 'Ogre Odor'), ('#43302E', 'Old Burgundy'), ('#CFB53B', 'Old Gold'), ('#563C5C', 'Old Heliotrope'), ('#FDF5E6', 'Old Lace'), ('#796878', 'Old Lavender'), ('#673147', 'Old Mauve'), ('#867E36', 'Old Moss Green'), ('#C08081', 'Old Rose'), ('#848482', 'Old Silver'), ('#808000', 'Olive'), ('#6B8E23', 'Olive Drab (#3)'), ('#3C341F', 'Olive Drab #7'), ('#9AB973', 'Olivine'), ('#353839', 'Onyx'), ('#B784A7', 'Opera Mauve'), ('#FF7F00', 'Orange (Color Wheel)'), ('#FF7538', 'Orange (Crayola)'), ('#FF5800', 'Orange (Pantone)'), ('#FB9902', 'Orange (RYB)'), ('#FFA500', 'Orange (Web)'), ('#FF9F00', 'Orange Peel'), ('#FF4500', 'Orange-Red'), ('#FA5B3D', 'Orange Soda'), ('#F8D568', 'Orange-Yellow'), ('#DA70D6', 'Orchid'), ('#F2BDCD', 'Orchid Pink'), ('#FB4F14', 'Orioles Orange'), ('#654321', 'Otter Brown'), ('#414A4C', 'Outer Space'), ('#FF6E4A', 'Outrageous Orange'), ('#002147', 'Oxford Blue'), ('#990000', 'OU Crimson Red'), ('#1CA9C9', 'Pacific Blue'), ('#006600', 'Pakistan Green'), ('#273BE2', 'Palatinate Blue'), ('#682860', 'Palatinate Purple'), ('#BCD4E6', 'Pale Aqua'), ('#AFEEEE', 'Pale Blue'), ('#987654', 'Pale Brown'), ('#AF4035', 'Pale Carmine'), ('#9BC4E2', 'Pale Cerulean'), ('#DDADAF', 'Pale Chestnut'), ('#DA8A67', 'Pale Copper'), ('#ABCDEF', 'Pale Cornflower Blue'), ('#87D3F8', 'Pale Cyan'), ('#E6BE8A', 'Pale Gold'), ('#EEE8AA', 'Pale Goldenrod'), ('#98FB98', 'Pale Green'), ('#DCD0FF', 'Pale Lavender'), ('#F984E5', 'Pale Magenta'), ('#FF99CC', 'Pale Magenta-Pink'), ('#FADADD', 'Pale Pink'), ('#DDA0DD', 'Pale Plum'), ('#DB7093', 'Pale Red-Violet'), ('#96DED1', 'Pale Robin Egg Blue'), ('#C9C0BB', 'Pale Silver'), ('#ECEBBD', 'Pale Spring Bud'), ('#BC987E', 'Pale Taupe'), ('#AFEEEE', 'Pale Turquoise'), ('#CC99FF', 'Pale Violet'), ('#DB7093', 'Pale Violet-Red'), ('#6F9940', 'Palm Leaf'), ('#78184A', 'Pansy Purple'), ('#009B7D', 'Paolo Veronese Green'), ('#FFEFD5', 'Papaya Whip'), ('#E63E62', 'Paradise Pink'), ('#50C878', 'Paris Green'), ('#D998A0', 'Parrot Pink'), ('#AEC6CF', 'Pastel Blue'), ('#836953', 'Pastel Brown'), ('#CFCFC4', 'Pastel Gray'), ('#77DD77', 'Pastel Green'), ('#F49AC2', 'Pastel Magenta'), ('#FFB347', 'Pastel Orange'), ('#DEA5A4', 'Pastel Pink'), ('#B39EB5', 'Pastel Purple'), ('#FF6961', 'Pastel Red'), ('#CB99C9', 'Pastel Violet'), ('#FDFD96', 'Pastel Yellow'), ('#800080', 'Patriarch'), ('#536878', "Payne's Grey"), ('#FFE5B4', 'Peach'), ('#FFCBA4', 'Peach'), ('#FFCC99', 'Peach-Orange'), ('#FFDAB9', 'Peach Puff'), ('#FADFAD', 'Peach-Yellow'), ('#D1E231', 'Pear'), ('#EAE0C8', 'Pearl'), ('#88D8C0', 'Pearl Aqua'), ('#B768A2', 'Pearly Purple'), ('#E6E200', 'Peridot'), ('#CCCCFF', 'Periwinkle'), ('#E12C2C', 'Permanent Geranium Lake'), ('#1C39BB', 'Persian Blue'), ('#00A693', 'Persian Green'), ('#32127A', 'Persian Indigo'), ('#D99058', 'Persian Orange'), ('#F77FBE', 'Persian Pink'), ('#701C1C', 'Persian Plum'), ('#CC3333', 'Persian Red'), ('#FE28A2', 'Persian Rose'), ('#EC5800', 'Persimmon'), ('#CD853F', 'Peru'), ('#8BA8B7', 'Pewter Blue'), ('#DF00FF', 'Phlox'), ('#000F89', 'Phthalo Blue'), ('#123524', 'Phthalo Green'), ('#45B1E8', 'Picton Blue'), ('#C30B4E', 'Pictorial Carmine'), ('#FDDDE6', 'Piggy Pink'), ('#01796F', 'Pine Green'), ('#563C0D', 'Pineapple'), ('#FFC0CB', 'Pink'), ('#D74894', 'Pink (Pantone)'), ('#FC74FD', 'Pink Flamingo'), ('#FFDDF4', 'Pink Lace'), ('#D8B2D1', 'Pink Lavender'), ('#FF9966', 'Pink-Orange'), ('#E7ACCF', 'Pink Pearl'), ('#980036', 'Pink Raspberry'), ('#F78FA7', 'Pink Sherbet'), ('#93C572', 'Pistachio'), ('#391285', 'Pixie Powder'), ('#E5E4E2', 'Platinum'), ('#8E4585', 'Plum'), ('#DDA0DD', 'Plum (Web)'), ('#5946B2', 'Plump Purple'), ('#5DA493', 'Polished Pine'), ('#86608E', 'Pomp And Power'), ('#BE4F62', 'Popstar'), ('#FF5A36', 'Portland Orange'), ('#B0E0E6', 'Powder Blue'), ('#FF85CF', 'Princess Perfume'), ('#F58025', 'Princeton Orange'), ('#701C1C', 'Prune'), ('#003153', 'Prussian Blue'), ('#DF00FF', 'Psychedelic Purple'), ('#CC8899', 'Puce'), ('#722F37', 'Puce Red'), ('#644117', 'Pullman Brown (UPS Brown)'), ('#3B331C', 'Pullman Green'), ('#FF7518', 'Pumpkin'), ('#800080', 'Purple (HTML)'), ('#9F00C5', 'Purple (Munsell)'), ('#A020F0', 'Purple (X11)'), ('#69359C', 'Purple Heart'), ('#9678B6', 'Purple Mountain Majesty'), ('#4E5180', 'Purple Navy'), ('#FE4EDA', 'Purple Pizzazz'), ('#9C51B6', 'Purple Plum'), ('#50404D', 'Purple Taupe'), ('#9A4EAE', 'Purpureus'), ('#51484F', 'Quartz'), ('#436B95', 'Queen Blue'), ('#E8CCD7', 'Queen Pink'), ('#A6A6A6', 'Quick Silver'), ('#8E3A59', 'Quinacridone Magenta'), ('#5D8AA8', 'Rackley'), ('#FF355E', 'Radical Red'), ('#242124', 'Raisin Black'), ('#FBAB60', 'Rajah'), ('#E30B5D', 'Raspberry'), ('#915F6D', 'Raspberry Glace'), ('#E25098', 'Raspberry Pink'), ('#B3446C', 'Raspberry Rose'), ('#D68A59', 'Raw Sienna'), ('#826644', 'Raw Umber'), ('#FF33CC', 'Razzle Dazzle Rose'), ('#E3256B', 'Razzmatazz'), ('#8D4E85', 'Razzmic Berry'), ('#663399', 'Rebecca Purple'), ('#FF0000', 'Red'), ('#EE204D', 'Red (Crayola)'), ('#F2003C', 'Red (Munsell)'), ('#C40233', 'Red (NCS)'), ('#ED2939', 'Red (Pantone)'), ('#ED1C24', 'Red (Pigment)'), ('#FE2712', 'Red (RYB)'), ('#A52A2A', 'Red-Brown'), ('#860111', 'Red Devil'), ('#FF5349', 'Red-Orange'), ('#E40078', 'Red-Purple'), ('#FD3A4A', 'Red Salsa'), ('#C71585', 'Red-Violet'), ('#A45A52', 'Redwood'), ('#522D80', 'Regalia'), ('#000000', 'Registration Black'), ('#002387', 'Resolution Blue'), ('#777696', 'Rhythm'), ('#004040', 'Rich Black'), ('#010B13', 'Rich Black (FOGRA29)'), ('#010203', 'Rich Black (FOGRA39)'), ('#F1A7FE', 'Rich Brilliant Lavender'), ('#D70040', 'Rich Carmine'), ('#0892D0', 'Rich Electric Blue'), ('#A76BCF', 'Rich Lavender'), ('#B666D2', 'Rich Lilac'), ('#B03060', 'Rich Maroon'), ('#444C38', 'Rifle Green'), ('#704241', 'Roast Coffee'), ('#00CCCC', 'Robin Egg Blue'), ('#8A7F80', 'Rocket Metallic'), ('#838996', 'Roman Silver'), ('#FF007F', 'Rose'), ('#F9429E', 'Rose Bonbon'), ('#9E5E6F', 'Rose Dust'), ('#674846', 'Rose Ebony'), ('#B76E79', 'Rose Gold'), ('#E32636', 'Rose Madder'), ('#FF66CC', 'Rose Pink'), ('#AA98A9', 'Rose Quartz'), ('#C21E56', 'Rose Red'), ('#905D5D', 'Rose Taupe'), ('#AB4E52', 'Rose Vale'), ('#65000B', 'Rosewood'), ('#D40000', 'Rosso Corsa'), ('#BC8F8F', 'Rosy Brown'), ('#0038A8', 'Royal Azure'), ('#002366', 'Royal Blue'), ('#4169E1', 'Royal Blue'), ('#CA2C92', 'Royal Fuchsia'), ('#7851A9', 'Royal Purple'), ('#FADA5E', 'Royal Yellow'), ('#CE4676', 'Ruber'), ('#D10056', 'Rubine Red'), ('#E0115F', 'Ruby'), ('#9B111E', 'Ruby Red'), ('#FF0028', 'Ruddy'), ('#BB6528', 'Ruddy Brown'), ('#E18E96', 'Ruddy Pink'), ('#A81C07', 'Rufous'), ('#80461B', 'Russet'), ('#679267', 'Russian Green'), ('#32174D', 'Russian Violet'), ('#B7410E', 'Rust'), ('#DA2C43', 'Rusty Red'), ('#00563F', 'Sacramento State Green'), ('#8B4513', 'Saddle Brown'), ('#FF7800', 'Safety Orange'), ('#FF6700', 'Safety Orange (Blaze Orange)'), ('#EED202', 'Safety Yellow'), ('#F4C430', 'Saffron'), ('#BCB88A', 'Sage'), ('#23297A', "St. Patrick's Blue"), ('#FA8072', 'Salmon'), ('#FF91A4', 'Salmon Pink'), ('#C2B280', 'Sand'), ('#967117', 'Sand Dune'), ('#ECD540', 'Sandstorm'), ('#F4A460', 'Sandy Brown'), ('#FDD9B5', 'Sandy Tan'), ('#967117', 'Sandy Taupe'), ('#92000A', 'Sangria'), ('#507D2A', 'Sap Green'), ('#0F52BA', 'Sapphire'), ('#0067A5', 'Sapphire Blue'), ('#FF4681', 'Sasquatch Socks'), ('#CBA135', 'Satin Sheen Gold'), ('#FF2400', 'Scarlet'), ('#FD0E35', 'Scarlet'), ('#FF91AF', 'Schauss Pink'), ('#FFD800', 'School Bus Yellow'), ('#66FF66', "Screamin' Green"), ('#006994', 'Sea Blue'), ('#9FE2BF', 'Sea Foam Green'), ('#2E8B57', 'Sea Green'), ('#4BC7CF', 'Sea Serpent'), ('#59260B', 'Seal Brown'), ('#FFF5EE', 'Seashell'), ('#FFBA00', 'Selective Yellow'), ('#704214', 'Sepia'), ('#8A795D', 'Shadow'), ('#778BA5', 'Shadow Blue'), ('#FFCFF1', 'Shampoo'), ('#009E60', 'Shamrock Green'), ('#8FD400', 'Sheen Green'), ('#D98695', 'Shimmering Blush'), ('#5FA778', 'Shiny Shamrock'), ('#FC0FC0', 'Shocking Pink'), ('#FF6FFF', 'Shocking Pink (Crayola)'), ('#882D17', 'Sienna'), ('#C0C0C0', 'Silver'), ('#ACACAC', 'Silver Chalice'), ('#5D89BA', 'Silver Lake Blue'), ('#C4AEAD', 'Silver Pink'), ('#BFC1C2', 'Silver Sand'), ('#CB410B', 'Sinopia'), ('#FF3855', 'Sizzling Red'), ('#FFDB00', 'Sizzling Sunrise'), ('#007474', 'Skobeloff'), ('#87CEEB', 'Sky Blue'), ('#CF71AF', 'Sky Magenta'), ('#6A5ACD', 'Slate Blue'), ('#708090', 'Slate Gray'), ('#003399', 'Smalt (Dark Powder Blue)'), ('#299617', 'Slimy Green'), ('#FF6D3A', 'Smashed Pumpkin'), ('#C84186', 'Smitten'), ('#738276', 'Smoke'), ('#832A0D', 'Smokey Topaz'), ('#100C08', 'Smoky Black'), ('#933D41', 'Smoky Topaz'), ('#FFFAFA', 'Snow'), ('#CEC8EF', 'Soap'), ('#893843', 'Solid Pink'), ('#757575', 'Sonic Silver'), ('#9E1316', 'Spartan Crimson'), ('#1D2951', 'Space Cadet'), ('#807532', 'Spanish Bistre'), ('#0070B8', 'Spanish Blue'), ('#D10047', 'Spanish Carmine'), ('#E51A4C', 'Spanish Crimson'), ('#989898', 'Spanish Gray'), ('#009150', 'Spanish Green'), ('#E86100', 'Spanish Orange'), ('#F7BFBE', 'Spanish Pink'), ('#E60026', 'Spanish Red'), ('#00FFFF', 'Spanish Sky Blue'), ('#4C2882', 'Spanish Violet'), ('#007F5C', 'Spanish Viridian'), ('#8B5f4D', 'Spicy Mix'), ('#0FC0FC', 'Spiro Disco Ball'), ('#A7FC00', 'Spring Bud'), ('#87FF2A', 'Spring Frost'), ('#00FF7F', 'Spring Green'), ('#007BB8', 'Star Command Blue'), ('#4682B4', 'Steel Blue'), ('#CC33CC', 'Steel Pink'), ('#5F8A8B', 'Steel Teal'), ('#FADA5E', 'Stil De Grain Yellow'), ('#990000', 'Stizza'), ('#4F666A', 'Stormcloud'), ('#E4D96F', 'Straw'), ('#FC5A8D', 'Strawberry'), ('#914E75', 'Sugar Plum'), ('#FF404C', 'Sunburnt Cyclops'), ('#FFCC33', 'Sunglow'), ('#F2F27A', 'Sunny'), ('#E3AB57', 'Sunray'), ('#FAD6A5', 'Sunset'), ('#FD5E53', 'Sunset Orange'), ('#CF6BA9', 'Super Pink'), ('#A83731', 'Sweet Brown'), ('#D2B48C', 'Tan'), ('#F94D00', 'Tangelo'), ('#F28500', 'Tangerine'), ('#FFCC00', 'Tangerine Yellow'), ('#E4717A', 'Tango Pink'), ('#FB4D46', 'Tart Orange'), ('#483C32', 'Taupe'), ('#8B8589', 'Taupe Gray'), ('#D0F0C0', 'Tea Green'), ('#F88379', 'Tea Rose'), ('#F4C2C2', 'Tea Rose'), ('#008080', 'Teal'), ('#367588', 'Teal Blue'), ('#99E6B3', 'Teal Deer'), ('#00827F', 'Teal Green'), ('#CF3476', 'Telemagenta'), ('#CD5700', 'Tenne (Tawny)'), ('#E2725B', 'Terra Cotta'), ('#D8BFD8', 'Thistle'), ('#DE6FA1', 'Thulian Pink'), ('#FC89AC', 'Tickle Me Pink'), ('#0ABAB5', 'Tiffany Blue'), ('#E08D3C', "Tiger's Eye"), ('#DBD7D2', 'Timberwolf'), ('#EEE600', 'Titanium Yellow'), ('#FF6347', 'Tomato'), ('#746CC0', 'Toolbox'), ('#FFC87C', 'Topaz'), ('#FD0E35', 'Tractor Red'), ('#808080', 'Trolley Grey'), ('#00755E', 'Tropical Rain Forest'), ('#CDA4DE', 'Tropical Violet'), ('#0073CF', 'True Blue'), ('#3E8EDE', 'Tufts Blue'), ('#FF878D', 'Tulip'), ('#DEAA88', 'Tumbleweed'), ('#B57281', 'Turkish Rose'), ('#40E0D0', 'Turquoise'), ('#00FFEF', 'Turquoise Blue'), ('#A0D6B4', 'Turquoise Green'), ('#00C5CD', 'Turquoise Surf'), ('#8A9A5B', 'Turtle Green'), ('#FAD6A5', 'Tuscan'), ('#6F4E37', 'Tuscan Brown'), ('#7C4848', 'Tuscan Red'), ('#A67B5B', 'Tuscan Tan'), ('#C09999', 'Tuscany'), ('#8A496B', 'Twilight Lavender'), ('#66023C', 'Tyrian Purple'), ('#0033AA', 'UA Blue'), ('#D9004C', 'UA Red'), ('#8878C3', 'Ube'), ('#536895', 'UCLA Blue'), ('#FFB300', 'UCLA Gold'), ('#3CD070', 'UFO Green'), ('#3F00FF', 'Ultramarine'), ('#4166F5', 'Ultramarine Blue'), ('#FF6FFF', 'Ultra Pink'), ('#FC6C85', 'Ultra Red'), ('#635147', 'Umber'), ('#FFDDCA', 'Unbleached Silk'), ('#5B92E5', 'United Nations Blue'), ('#B78727', 'University Of California Gold'), ('#FFFF66', 'Unmellow Yellow'), ('#014421', 'UP Forest Green'), ('#7B1113', 'UP Maroon'), ('#AE2029', 'Upsdell Red'), ('#E1AD21', 'Urobilin'), ('#004F98', 'USAFA Blue'), ('#990000', 'USC Cardinal'), ('#FFCC00', 'USC Gold'), ('#F77F00', 'University Of Tennessee Orange'), ('#D3003F', 'Utah Crimson'), ('#664228', 'Van Dyke Brown'), ('#F3E5AB', 'Vanilla'), ('#F38FA9', 'Vanilla Ice'), ('#C5B358', 'Vegas Gold'), ('#C80815', 'Venetian Red'), ('#43B3AE', 'Verdigris'), ('#E34234', 'Vermilion'), ('#D9381E', 'Vermilion'), ('#A020F0', 'Veronica'), ('#74BBFB', 'Very Light Azure'), ('#6666FF', 'Very Light Blue'), ('#64E986', 'Very Light Malachite Green'), ('#FFB077', 'Very Light Tangelo'), ('#FFDFBF', 'Very Pale Orange'), ('#FFFFBF', 'Very Pale Yellow'), ('#8F00FF', 'Violet'), ('#7F00FF', 'Violet (Color Wheel)'), ('#8601AF', 'Violet (RYB)'), ('#EE82EE', 'Violet (Web)'), ('#324AB2', 'Violet-Blue'), ('#F75394', 'Violet-Red'), ('#40826D', 'Viridian'), ('#009698', 'Viridian Green'), ('#7C9ED9', 'Vista Blue'), ('#CC9900', 'Vivid Amber'), ('#922724', 'Vivid Auburn'), ('#9F1D35', 'Vivid Burgundy'), ('#DA1D81', 'Vivid Cerise'), ('#00AAEE', 'Vivid Cerulean'), ('#CC0033', 'Vivid Crimson'), ('#FF9900', 'Vivid Gamboge'), ('#A6D608', 'Vivid Lime Green'), ('#00CC33', 'Vivid Malachite'), ('#B80CE3', 'Vivid Mulberry'), ('#FF5F00', 'Vivid Orange'), ('#FFA000', 'Vivid Orange Peel'), ('#CC00FF', 'Vivid Orchid'), ('#FF006C', 'Vivid Raspberry'), ('#F70D1A', 'Vivid Red'), ('#DF6124', 'Vivid Red-Tangelo'), ('#00CCFF', 'Vivid Sky Blue'), ('#F07427', 'Vivid Tangelo'), ('#FFA089', 'Vivid Tangerine'), ('#E56024', 'Vivid Vermilion'), ('#9F00FF', 'Vivid Violet'), ('#FFE302', 'Vivid Yellow'), ('#CEFF00', 'Volt'), ('#34B233', 'Wageningen Green'), ('#004242', 'Warm Black'), ('#A4F4F9', 'Waterspout'), ('#7C98AB', 'Weldon Blue'), ('#645452', 'Wenge'), ('#F5DEB3', 'Wheat'), ('#FFFFFF', 'White'), ('#F5F5F5', 'White Smoke'), ('#A2ADD0', 'Wild Blue Yonder'), ('#D470A2', 'Wild Orchid'), ('#FF43A4', 'Wild Strawberry'), ('#FC6C85', 'Wild Watermelon'), ('#FD5800', 'Willpower Orange'), ('#A75502', 'Windsor Tan'), ('#722F37', 'Wine'), ('#673147', 'Wine Dregs'), ('#FF007C', 'Winter Sky'), ('#A0E6FF', 'Winter Wizard'), ('#56887D', 'Wintergreen Dream'), ('#C9A0DC', 'Wisteria'), ('#C19A6B', 'Wood Brown'), ('#738678', 'Xanadu'), ('#0F4D92', 'Yale Blue'), ('#1C2841', 'Yankees Blue'), ('#FFFF00', 'Yellow'), ('#FCE883', 'Yellow (Crayola)'), ('#EFCC00', 'Yellow (Munsell)'), ('#FFD300', 'Yellow (NCS)'), ('#FEDF00', 'Yellow (Pantone)'), ('#FFEF00', 'Yellow (Process)'), ('#FEFE33', 'Yellow (RYB)'), ('#9ACD32', 'Yellow-Green'), ('#FFAE42', 'Yellow Orange'), ('#FFF000', 'Yellow Rose'), ('#FFF700', 'Yellow Sunshine'), ('#0014A8', 'Zaffre'), ('#2C1608', 'Zinnwaldite Brown'), ('#39A78E', 'Zomp')], default='#0048BA', max_length=15),
        ),
        migrations.AlterField(
            model_name='svg_post',
            name='font',
            field=models.CharField(choices=[('SpaceGrotesk-Bold, Space Grotesk', 'SpaceGrotesk-Bold, Space Grotesk'), ('Akira Expanded', 'Akira Expanded'), ('SweetSnow', 'SweetSnow'), ('HKGrotesk', 'HKGrotesk')], default='SpaceGrotesk-Bold, Space Grotesk', max_length=100),
        ),
        migrations.AlterField(
            model_name='svg_post',
            name='tag',
            field=models.CharField(choices=[('Cool', 'Cool'), ('Sexy', 'Sexy'), ('Oriental', 'Oriental')], default='Cool', max_length=100),
        ),
    ]
