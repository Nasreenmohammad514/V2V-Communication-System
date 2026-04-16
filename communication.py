def broadcast_message(sender, vehicles, range_limit=20):
    """
    Sender vehicle message ni nearby vehicles ki pampisthundi
    """
    for vehicle in vehicles:
        # Sender ki thane message pampakudadhu
        if vehicle.vehicle_id != sender.vehicle_id:
            
            # Distance calculate cheyyadam
            distance = abs(vehicle.position - sender.position)

            # Range lo unte message receive chesthundi
            if distance <= range_limit:
                vehicle.receive_message(sender.message)
