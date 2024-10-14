import rclpy
import pygame

from rclpy.node import Node

from std_msgs.msg import Int32

class SoundPlayerClass(Node):

    def __init__(self):

        super().__init__('sound_player')

        self.subscription = self.create_subscription(
            Int32,
            'sound',
            self.listener_callback,
            10)
        
        self.subscription  # prevent unused variable warning
        self.i = 0

        pygame.init()
        #pygame.mixer.music.load('/home/ubunutu/Documents/Python/Sound/Pygame/cursor.mp3')
        pygame.mixer.music.load('/home/ubunutu/Music/mixkit-arcade-video-game-explosion-2810.wav')
        pygame.mixer.music.set_volume(5.0)

    def listener_callback(self, msg):
        if(msg.data == 0):
            pygame.mixer.music.load('/home/ubunutu/Music/damege.mp3')
        if(msg.data == 1):
            pygame.mixer.music.load('/home/ubunutu/Music/get.mp3')

        pygame.mixer.music.play(0)
        

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = SoundPlayerClass()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()