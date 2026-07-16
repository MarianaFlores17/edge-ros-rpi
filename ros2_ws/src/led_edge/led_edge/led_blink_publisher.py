class LedControlPublisher(Node):
    """Publica True/False alternado en /led_cmd a 1 Hz."""

    def __init__(self):
        super().__init__('led_edge_node')
        self.publisher_ = self.create_publisher(Bool, 'led_cmd', 10)
        self.subscription = self.create_subscription(String, 'topic', self.listener_callback, 10)
        self.subscription # Prevent unused variable warning
        self.state = False # Led state
        self.get_logger().info('led_edge_node listo, publicando en /led_cmd')

    def listener_callback(self, msg):
        """Alterna el estado y publica el mensaje."""
        # Imprimimos mensaje que se escucho
        self.get_logger().info(f'Recibido: "{msg}"')
        # Convertimos el mensaje String -> Bool  
        self.state = not self.state
        esp32_msg = Bool()
        esp32_msg.data = self.state
        # Publicamos el mensaje Bool al ESP32
        self.publisher_.publish(esp32_msg)
        self.get_logger().info(f'Publicado: {"ON" if esp32_msg.data else "OFF"}')