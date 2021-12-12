export interface Vehicle{
    id: any;
    due_date: string;
    posting_date: string;
    vin: string;
    manufacturer: string;
    brand: string;
    model:string;
    series: string;
    year: number;
    fuel_type: string;
    vehicle_type: string;
    body_class: string;
    base_price: number;
    engine: string;
    brake_system: string;
    number_cylinders: number;
    displacement_cc: number;
    doors: number;
    sells_history: [{
        sell_date: string;
        seller: string;
        sell_location: string;
        price: number;
        vehicle_mileage: string;
        vehicle_color: string;
    }]
  }