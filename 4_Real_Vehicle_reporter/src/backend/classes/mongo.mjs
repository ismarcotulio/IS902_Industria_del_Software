import { MongoClient } from 'mongodb'
class Mongo{

    constructor(){
        this.url = "mongodb+srv://grupounois601:grupounois601@cluster0.jwzk2.mongodb.net/CarDealership_OLTP2?retryWrites=true&w=majority"
        this.client = new MongoClient(this.url)
        this.conn = null
        
        this.startConexion()
    }    
    
    async startConexion(){
        console.log('Connected successfully to server');
        this.conn = await this.client.connect();
        return this.conn
    }

    getVehicleInfo(vin){
        return new Promise(async (resolve, reject)=>{
            const collection = db.collection('vehicles');
            const filteredVehicle = await collection.find({ vin: vin }).toArray();
            console.log('Found documents filtered by { vin:  } =>', filteredVehicle);
            resolve(filteredVehicle)
        })
      }
  
}

export { Mongo }