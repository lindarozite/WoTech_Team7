//version 1
//Message Controller

package com.datorium.Datorium.API.Controllers;

import com.datorium.Datorium.API.Services.MessageService;
import com.datorium.Datorium.API.DTOs.Message;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/message")

public class MessageController {
    private MessageService messageService;
    public MessageController() {
        messageService = new MessageService();

    }
    @PostMapping("/addmessage") // http://localhost:8080/message/addmessage
    public String add(@RequestBody Message message) {
        return messageService.add(message);
    }
}

//Message
package com.datorium.Datorium.API.DTOs;

public class Message {
    private String text;

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
}

//Message Service
package com.datorium.Datorium.API.Services;

import com.datorium.Datorium.API.DTOs.Message;

public class MessageService {

    public String add(Message message) {
        return message.getText();
    }
}

//version2
//Message
package com.datorium.Datorium.API.DTOs;

public class Message {
    public String message;
}

//Message Service
package com.datorium.Datorium.API.Services;

import com.datorium.Datorium.API.DTOs.Message;

public class MessageService {
    public String add(Message message){
        return message.message;
    }
}

//Message Controller
package com.datorium.Datorium.API.Controllers;

import com.datorium.Datorium.API.DTOs.Message;
import com.datorium.Datorium.API.Services.MessageService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/message")
    public class MessageController {
        private MessageService messageService;
        public MessageController(){
            messageService = new MessageService();
        }
    @PostMapping("/add") // localhost:808/test
        public String add(@RequestBody Message message){
            return messageService.add(message);
        }
    }

