import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReporterViewComponent } from './reporter-view.component';

describe('ReporterViewComponent', () => {
  let component: ReporterViewComponent;
  let fixture: ComponentFixture<ReporterViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ReporterViewComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ReporterViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
