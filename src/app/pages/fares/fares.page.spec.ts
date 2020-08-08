import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { FaresPage } from './fares.page';

describe('FaresPage', () => {
  let component: FaresPage;
  let fixture: ComponentFixture<FaresPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FaresPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(FaresPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
