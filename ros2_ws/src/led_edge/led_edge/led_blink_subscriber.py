#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class LedControlSubscriber(Node):

    def __init__(self):
        super().__init__('led_blink_subscriber')
        self.subscription = self.create_subscription(
            Bool,
            'led_cmd',
            self.listener_callback,
            10)
        self.subscription  # evitar advertencia de variable no usada
        self.get_logger().info('Nodo Receptor de Control de LED Iniciado...')

    def listener_callback(self, msg):
        self.get_logger().info(f'Recibido en /led_cmd: {msg.data}')
        if msg.data:
            self.get_logger().info(' -> Acción: ¡Encendiendo el LED! (Señal HIGH)')
        else:
            self.get_logger().info(' -> Acción: ¡Apagando el LED! (Señal LOW)')

def main(args=None):
    rclpy.init(args=args)
    node = LedControlSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()