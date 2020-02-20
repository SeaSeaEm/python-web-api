import { Injectable } from '@angular/core';

import { HttpClient } from "@angular/common/http";

@Injectable()
export class NfsService {
    private url = `http://127.0.0.1:5000/api/nfs`;

    constructor(private http: HttpClient) { }

    getMachineById(uuid: string): any {
        const obj = {
            "uuid": uuid
        }

        console.log(obj);

        return this.http.post(`${this.url}/single`, obj);
    }
}