import { Component, OnInit } from '@angular/core';

import { NfsService } from 'src/app/services/nfs.services';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  constructor(private nfsService: NfsService, ) { }

  ngOnInit() {
    const uuid: string = "1d0135b5-531f-11ea-b831-641c676a6d02";
    this.nfsService.getMachineById(uuid).subscribe(result => {
      console.log(result);
    });
  }
}
