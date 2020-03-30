package QLS;

/**
 * Tapchi
 */
public class Tapchi extends Sach {

    private int so_PH;
    private int Thang_PH;

    public Tapchi(String Ten_tai_lieu, int Ma_tai_lieu, String nha_XB, int So_ban_PH, int type, String TacGia,
            int Sotrang, int NamXB, int so_PH, int Thang_PH) {
        super(Ten_tai_lieu, Ma_tai_lieu, nha_XB, So_ban_PH, type, TacGia, Sotrang, NamXB);
        this.so_PH = so_PH;
        this.Thang_PH= Thang_PH;
    }

    public int so_PH(){
        return this.so_PH;
    }
    public int Thang_PH(){
        return this.Thang_PH;
    }

    public void setType() {
        int type = 2;
        this.setType(type);
    }

    
}