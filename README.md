# SertifyMe - Ceritificate Generator


'''
    # Successfully made certificate
    if filename != -1:
        email_certi( filename, i[1] )
        print("Sent to " + i[0])
    # Add to error list
    else:
        error_list.append(i[0])
        error_count += 1

    # Print all failed IDs
    print(str(error_count) + " Errors- List:" + ','.join(error_list))
'''


'''
# temp 1 

# Load font
    font = ImageFont.truetype('Fonts/CaveatBrush-Regular.ttf', 60)

    # Check sizes and if it is needed to be shortened
    if ( len( new_name ) > 20 ):
        new_name = shorten( new_name, 20 )
 
    # Insert text into image template for name
    location = (720, 345)
    text_color = (0, 137, 209)
    draw.text(location, new_name, fill = text_color, font = font)

## temp 2 

    # Load font
    font = ImageFont.truetype('Fonts/CaveatBrush-Regular.ttf', 60)

    # Check sizes and if it is needed to be shortened
    if ( len( new_name ) > 20 ):
        new_name = shorten( new_name, 20 )
 
    # Insert text into image template for name
    location = (720, 345)
    text_color = (0, 137, 209)
    draw.text(location, new_name, fill = text_color, font = font)

    # font for speaker
    font_s = ImageFont.truetype('Fonts/CourierPrime-Regular.ttf', 20)
    speaker_name = 'Samriddhi Agarwal'

    # Insert text into image template for speaker
    location_s = (120, 590) # need to edit
    text_color_s = (164, 226, 228)
    draw.text(location_s, speaker_name, fill = text_color_s, font = font_s)

    # font for speaker position
    font_p = ImageFont.truetype('Fonts/Lato-Regular.ttf', 16)
    position_name = 'CEO SertifyMe'

    # Insert text into image template for speaker position
    location_p = (120, 645)  # need to edit
    text_color_p = (0, 112, 192)
    draw.text(location_p, position_name, fill = text_color_p, font = font_p)
'''