package admin

import (
	"fmt"
	"os"
)

// change path if don run
var path string = "...."

func main() {
	file, err := os.Create(path)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	fmt.Println("Hello world")

}
