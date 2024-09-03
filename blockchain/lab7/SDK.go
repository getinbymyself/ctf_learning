package main
import (
	"log"
	"net/http"
	"fmt"
	"github.com/hyperledger/fabric-sdk-go/pkg/client/channel"
	"github.com/hyperledger/fabric-sdk-go/pkg/core/config"
	"github.com/hyperledger/fabric-sdk-go/pkg/fabsdk"
	"github.com/gin-gonic/gin"
)
type Car struct {
	CarNumber string `json:"carnumber"`
	Make   string `json:"make"`
	Model  string `json:"model"`
	Colour string `json:"colour"`
	Owner  string `json:"owner"`
}
var (
	SDK        *fabsdk.FabricSDK
	channelClient *channel.Client
	channelName = "mychannel"
	chaincodeName = "fabcar"
	orgName  = "Org1"
	orgAdmin = "Admin"
	org1Peer0 = "peer0.org1.example.com"
	org2Peer0 = "peer0.org2.example.com"
)
func ChannelExecute(funcName string, args [][]byte)(channel.Response,error){
	var err error
	configPath := "./config.yaml"
	configProvider := config.FromFile(configPath)
	SDK,err = fabsdk.New(configProvider)
	if err != nil{
		log.Fatalf("Failed to create new SDK: %s", err)
	} 
	ctx := SDK.ChannelContext(channelName,fabsdk.WithOrg(orgName),fabsdk.WithUser(orgAdmin))
	channelClient,err = channel.New(ctx)
	response,err := channelClient.Execute(channel.Request{
		ChaincodeID : chaincodeName,
		Fcn : funcName,
		Args: args,
	})
	if err != nil{
		return response,err
	}
	SDK.Close()
	return response,nil
}
func main(){
	r := gin.Default()
	r.GET("/queryAllCars",func(c *gin.Context){
		var result channel.Response
		result,err := ChannelExecute("queryAllCars",[][]byte{})
		fmt.Println(result)
		if err != nil{
			log.Fatalf("Failed to evaluate transaction: %s\n", err)
		}
		c.JSON(http.StatusOK,gin.H{
			"code" : "200",
			"message" : "Query All Success",
			"result" : string(result.Payload),
		})
	})
	r.POST("/createCar",func(c *gin.Context){
		var car Car
		c.BindJSON(&car)
		var result channel.Response
		result,err := ChannelExecute("CreateCar",[][]byte{[]byte(car.CarNumber),[]byte(car.Make),[]byte(car.Model),[]byte(car.Colour),[]byte(car.Owner)})
		fmt.Println(result)
		if err != nil{
			log.Fatalf("Failed to evaluate transaction: %s\n", err)
		}
		c.JSON(http.StatusOK,gin.H{
			"code" : "200",
			"message" : "Create Success",
			"result" : string(result.Payload),
		})
	})
	r.POST("/queryCar",func(c *gin.Context){
		var car Car
		c.BindJSON(&car)
		var result channel.Response
		result,err := ChannelExecute("QueryCar",[][]byte{[]byte(car.CarNumber)})
		fmt.Println(result)
		if err != nil{
			log.Fatalf("Failed to evaluate transaction: %s\n", err)
		}
		c.JSON(http.StatusOK,gin.H{
			"code" : "200",
			"message" : "Query Success",
			"result" : string(result.Payload),
		})
	})
	r.Run(":9099")
}