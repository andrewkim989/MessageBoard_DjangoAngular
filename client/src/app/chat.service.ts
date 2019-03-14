
import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ChatService {

  constructor(private _http: HttpClient) { }

  allThreads() {
    return this._http.get("/thread");
  }

  newThread(thread) {
    return this._http.post("/thread", thread);
  }

  showThread(id) {
    return this._http.get("/thread/" + id);
  }

  newComment(id, comment) {
    return this._http.post("/thread/" + id, comment);
  }
}
