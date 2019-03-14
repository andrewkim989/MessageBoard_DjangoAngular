import { Component, OnInit } from '@angular/core';
import { ChatService } from "../chat.service";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  threads: any;
  comments: any;
  newthread: any;
  data: any;
  error: boolean = false;

  constructor(private chatService: ChatService) { }

  ngOnInit() {
    this.newthread = {name: "", subject: "", post: ""};
    this.getThreads();
  }

  getThreads() {
    let t = this.chatService.allThreads();
    t.subscribe(data => {
      this.threads = data["threads"].reverse();
    });
  }

  createThread() {
    let c = this.chatService.newThread({name: this.newthread.name, subject: this.newthread.subject,
      post: this.newthread.post});
    c.subscribe(data => {
      this.data = data;
      if (this.data.error) {
        this.error = true;
      }
      else {
        this.error = false;
        this.newthread = {name: "", subject: "", post: ""};
      }
      this.getThreads();
    });
  }
}
