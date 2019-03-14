import { Component, OnInit } from '@angular/core';
import { ChatService } from "../chat.service";
import { ActivatedRoute } from "@angular/router";

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {
  thread: any;
  comments: any;
  id: string;
  newcomment: any;

  constructor(private chatService: ChatService, private _route: ActivatedRoute) { }

  ngOnInit() {
    this.id = this._route.snapshot.params["id"];
    this.getThread();
    this.newcomment = {name: "", post: ""};
  }

  getThread() {
    let t = this.chatService.showThread(this.id);
    t.subscribe(data => {
      this.thread = data["thread"];
      this.comments = data["comments"];
      console.log(this.comments);
    });
  }

  postComment() {
    let c = this.chatService.newComment(this.id, {name: this.newcomment.name, post: this.newcomment.post});
    c.subscribe(data => {
      console.log(data);
      this.newcomment = {name: "", post: ""};
      this.getThread();
    })
  }
}