package QLS;

/**
 * TaiLieu
 */
public class TaiLieu {
    //Declare data
    private String Ten_tai_lieu;
    private int Ma_tai_lieu;
    private String nha_XB;
    private int So_ban_PH=0;
    private int type;

    public TaiLieu(String Ten_tai_lieu, int Ma_tai_lieu, String nha_XB, int So_ban_PH,int type) {
        this.Ten_tai_lieu    = Ten_tai_lieu;
        this.Ma_tai_lieu  = Ma_tai_lieu;
        this.nha_XB   = nha_XB;
        this.So_ban_PH = So_ban_PH;
        this.type = type;
    }
  
    public String getTen_tai_lieu() {
        return this.Ten_tai_lieu;
    }
  
    public int getMa_tai_lieu() {
        return this.Ma_tai_lieu;
    }
  
    public String getNha_XB() {
        return this.nha_XB;
    }
  
    public int getSo_ban_PH() {
        return this.So_ban_PH;
    }
  
    public void setSbph(int So_ban_PH) {
        this.So_ban_PH= So_ban_PH;
    }

    public int getType() {
        return this.type;
    }
  
    public void setType(int type){
        this.type = type;
    } 

    public String toS() {
        return "'" + Ten_tai_lieu + "' by" + nha_XB;
    } 

}