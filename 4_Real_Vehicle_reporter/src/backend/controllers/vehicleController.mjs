class VehicleController{

    constructor(database){
        this.database = database
    }

    getVehicleInfo(req,res,vin){
        (async()=>{
            this.database.getVehicleInfo(vin)
            .then(results=>{
                if(results!=false){
                    return res.send(results)
                }else{
                    return res.send(false)
                }
            })
        })();
    }
}

export {VehicleController}