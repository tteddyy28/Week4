import arcade


def main():
    arcade.open_window(1000, 1000, "My Picture")
    arcade.set_background_color(arcade.color.WHITE)
    #create objects
    rubrix_cube = arcade.create_rectangle(500, 500, 500, 500, arcade.color.WHITE)
    individual_square_1 = arcade.create_rectangle(500, 500, 175, 175, arcade.color.BLUE)#second row middle piece
    individual_square_2 = arcade.create_rectangle(328, 500, 150, 175, arcade.color.BLUE)#second row left side piece
    individual_square_3 = arcade.create_rectangle(672, 500, 150, 175, arcade.color.BLUE)#second row right side piece
    individual_square_4 = arcade.create_rectangle(500, 670, 175, 150, arcade.color.BLUE)#top row middle peiece
    individual_square_5 = arcade.create_rectangle(672, 670, 150, 150, arcade.color.BLUE)#top row right side piece
    individual_square_6 = arcade.create_rectangle(328, 670, 150, 150, arcade.color.BLUE)#top row left side piece
    individual_square_7 = arcade.create_rectangle(500, 330, 175, 150, arcade.color.BLUE)#bottom row middle piece
    individual_square_8 = arcade.create_rectangle(672, 330, 150, 150, arcade.color.BLUE)#bottom right side piece
    individual_square_9 = arcade.create_rectangle(328, 330, 150, 150, arcade.color.BLUE)#bottom left side piece
    spikes = arcade.draw_triangle_filled(50, 50, 75, 75, 60, 60, arcade.color.RED)



    arcade.start_render()
    #Draw Everything
    rubrix_cube.draw()
    individual_square_1.draw()
    individual_square_2.draw()
    individual_square_3.draw()
    individual_square_4.draw()
    individual_square_5.draw()
    individual_square_6.draw()
    individual_square_7.draw()
    individual_square_8.draw()
    individual_square_9.draw()
    spikes.draw()
    arcade.finish_render()

    arcade.run()



main()