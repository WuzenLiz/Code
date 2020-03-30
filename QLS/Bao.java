package QLS;

/**
 * Bao
 */
public class Bao extends Tapchi{

    private int Ngay_PH;

    public Bao(String Ten_tai_lieu, int Ma_tai_lieu, String nha_XB, int So_ban_PH, int type, String TacGia, int Sotrang,
            int NamXB, int so_PH, int Thang_PH, int Ngay_PH) {
        super(Ten_tai_lieu, Ma_tai_lieu, nha_XB, So_ban_PH, type, TacGia, Sotrang, NamXB, so_PH, Thang_PH);
        this.Ngay_PH = Ngay_PH;
    }
    
    public int Ngay_PH(){
        return this.Ngay_PH;
    }

    public void setType() {
        int type = 3;
        this.setType(type);
    }
    
}