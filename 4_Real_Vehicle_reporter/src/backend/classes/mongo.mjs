import { MongoClient } from 'mongodb'
class Mongo{

    constructor(){
        this.url = "mongodb+srv://grupounois601:grupounois601@cluster0.jwzk2.mongodb.net/?retryWrites=true&w=majority"
        this.client = new MongoClient(this.url)
        this.db = null
        
        this.startConexion()
    }    
    
    async startConexion(){
        console.log('Connected successfully to server');
        await this.client.connect();
        this.db = this.client.db("CarDealership_OLTP2");
    }

    getVehicleInfo(vin){
        return new Promise(async (resolve, reject)=>{
            console.log(this.db)
            let collection = this.db.collection('vehicles');
            let filteredVehicle = await collection.find({ vin: vin }).toArray();
            console.log('Found documents filtered by { vin:  } =>', filteredVehicle);
            resolve(filteredVehicle)
        })
      }
  
}

export { Mongo }